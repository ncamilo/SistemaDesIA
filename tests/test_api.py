import pytest
from fastapi.testclient import TestClient

from app.main import create_app


def add_task(client, project_id, title="Conferir componentes"):
    response = client.post(f"/api/projects/{project_id}/tasks", json={"title": title})
    assert response.status_code == 201
    return response.json()


def test_project_crud(client):
    assert client.get("/api/projects").json() == []
    response = client.post(
        "/api/projects",
        json={"title": "  Painel  ", "customer": " Cliente ", "order_reference": "PED-001"},
    )
    assert response.status_code == 201
    project = response.json()
    path = f"/api/projects/{project['id']}"
    assert project["title"] == "Painel"
    assert project["customer"] == "Cliente"
    assert project["status"] == "pending"
    assert client.get(path).json() == project
    assert client.get("/api/projects").json() == [project]
    response = client.patch(path, json={"title": "Painel revisado", "description": "24 V"})
    assert response.status_code == 200
    assert response.json()["customer"] == "Cliente"
    assert client.get(path).json()["description"] == "24 V"
    assert client.delete(path).status_code == 204
    assert client.get(path).status_code == 404


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"title": "Painel"},
        {"title": " ", "customer": "Cliente"},
        {"title": "Painel", "customer": "\t "},
        {"title": "a" * 121, "customer": "Cliente"},
        {"title": "Painel", "customer": "Cliente", "order_reference": "a" * 81},
        {"title": "Painel", "customer": "Cliente", "description": "a" * 2001},
        {"title": "Painel", "customer": "Cliente", "status": "done"},
    ],
)
def test_invalid_project_rejected(client, payload):
    assert client.post("/api/projects", json=payload).status_code == 422
    assert client.get("/api/projects").json() == []


@pytest.mark.parametrize("payload", [{}, {"title": None}, {"customer": " "}, {"status": "done"}])
def test_invalid_project_patch_does_not_modify_data(client, project, payload):
    path = f"/api/projects/{project['id']}"
    assert client.patch(path, json=payload).status_code == 422
    assert client.get(path).json() == project


def test_tasks_lifecycle_and_project_progress(client, project):
    pid = project["id"]
    first = add_task(client, pid)
    second = add_task(client, pid, "Montar painel")
    assert first["status"] == "pending"
    assert first["project_id"] == pid
    path = f"/api/tasks/{first['id']}"
    assert client.patch(path, json={"status": "in_progress"}).status_code == 200
    assert client.get(f"/api/projects/{pid}").json()["status"] == "in_progress"
    response = client.patch(path, json={"title": "Conferência final", "status": "done"})
    assert response.json()["title"] == "Conferência final"
    assert client.get(f"/api/projects/{pid}").json()["progress"] == 50
    client.patch(f"/api/tasks/{second['id']}", json={"status": "done"})
    complete = client.get(f"/api/projects/{pid}").json()
    assert (complete["status"], complete["progress"]) == ("done", 100)
    client.patch(path, json={"status": "pending"})
    reopened = client.get(f"/api/projects/{pid}").json()
    assert (reopened["status"], reopened["progress"]) == ("in_progress", 50)
    assert client.delete(path).status_code == 204
    assert client.get(f"/api/projects/{pid}").json()["progress"] == 100
    client.delete(f"/api/tasks/{second['id']}")
    empty = client.get(f"/api/projects/{pid}").json()
    assert (empty["status"], empty["progress"], empty["total_tasks"]) == ("pending", 0, 0)


def test_new_task_reopens_completed_project(client, project):
    task = add_task(client, project["id"])
    client.patch(f"/api/tasks/{task['id']}", json={"status": "done"})
    add_task(client, project["id"], "Inspeção adicional")
    result = client.get(f"/api/projects/{project['id']}").json()
    assert result["status"] == "in_progress"
    assert result["progress"] == 50


def test_project_isolation_and_status_filter(client, project):
    pid = project["id"]
    other = client.post("/api/projects", json={"title": "Outro", "customer": "Outro"}).json()
    add_task(client, other["id"], "Não deve aparecer")
    pending = add_task(client, pid)
    done = add_task(client, pid)
    client.patch(f"/api/tasks/{done['id']}", json={"status": "done"})
    assert len(client.get(f"/api/projects/{pid}/tasks").json()) == 2
    result = client.get(f"/api/projects/{pid}/tasks?status=pending").json()
    assert [task["id"] for task in result] == [pending["id"]]
    assert client.get(f"/api/projects/{pid}/tasks?status=in_progress").json() == []
    assert client.get(f"/api/projects/{pid}/tasks?status=invalid").status_code == 422


@pytest.mark.parametrize(
    "payload", [{}, {"status": "invalid"}, {"status": None}, {"title": " "}, {"project_id": 999}]
)
def test_invalid_task_patch_keeps_task_unchanged(client, project, payload):
    task = add_task(client, project["id"])
    assert client.patch(f"/api/tasks/{task['id']}", json=payload).status_code == 422
    assert client.get(f"/api/projects/{project['id']}/tasks").json() == [task]


@pytest.mark.parametrize("payload", [{}, {"title": " "}, {"title": "a" * 121}])
def test_invalid_task_creation(client, project, payload):
    path = f"/api/projects/{project['id']}/tasks"
    assert client.post(path, json=payload).status_code == 422
    assert client.get(path).json() == []


def test_project_with_tasks_cannot_be_deleted(client, project):
    task = add_task(client, project["id"])
    path = f"/api/projects/{project['id']}"
    assert client.delete(path).status_code == 409
    assert client.get(path).status_code == 200
    client.delete(f"/api/tasks/{task['id']}")
    assert client.delete(path).status_code == 204


@pytest.mark.parametrize(
    "method, path, payload",
    [
        ("get", "/api/projects/999", None),
        ("patch", "/api/projects/999", {"title": "Novo"}),
        ("delete", "/api/projects/999", None),
        ("get", "/api/projects/999/tasks", None),
        ("post", "/api/projects/999/tasks", {"title": "Tarefa"}),
        ("patch", "/api/tasks/999", {"status": "done"}),
        ("delete", "/api/tasks/999", None),
    ],
)
def test_missing_resources(client, method, path, payload):
    response = client.request(method, path, **({"json": payload} if payload else {}))
    assert response.status_code == 404


def test_data_survives_application_restart(tmp_path):
    url = f"sqlite:///{tmp_path / 'persistent.db'}"
    with TestClient(create_app(url)) as first:
        project = first.post(
            "/api/projects", json={"title": "Painel", "customer": "Cliente"}
        ).json()
        task = add_task(first, project["id"])
        first.patch(f"/api/tasks/{task['id']}", json={"status": "done"})
    with TestClient(create_app(url)) as second:
        restored = second.get(f"/api/projects/{project['id']}").json()
        assert restored["title"] == "Painel"
        assert restored["progress"] == 100
        assert restored["status"] == "done"
        assert second.get(f"/api/projects/{project['id']}/tasks").json()[0]["id"] == task["id"]


def test_web_and_openapi_are_available(client):
    assert "Organize cada montagem" in client.get("/").text
    assert client.get("/static/app.js").status_code == 200
    assert client.get("/static/style.css").status_code == 200
    assert "/api/projects" in client.get("/openapi.json").json()["paths"]
