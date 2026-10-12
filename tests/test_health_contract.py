from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.main import create_app
from app.repositories import Repository
from app.schemas import ErrorResponse


def test_runtime_database_failure_is_safe_and_next_request_recovers(client):
    with patch.object(
        Repository,
        "projects",
        side_effect=OperationalError("SELECT segredo", {}, Exception("cliente privado")),
    ):
        response = client.get("/api/projects")
    assert response.status_code == 503
    assert response.json() == {"detail": "Banco de dados indisponível."}
    assert client.get("/health").status_code == 200
    assert client.get("/api/projects").json() == []


def test_failed_commit_does_not_persist_project(client):
    from sqlalchemy.orm import Session

    with patch.object(Session, "commit", side_effect=OperationalError("INSERT", {}, Exception())):
        response = client.post("/api/projects", json={"title": "Teste", "customer": "Fictício"})
    assert response.status_code == 503
    assert client.get("/api/projects").json() == []
    assert (
        client.post("/api/projects", json={"title": "Novo", "customer": "Teste"}).status_code == 201
    )


def test_database_failure_at_startup_does_not_block_liveness(tmp_path):
    # SQLite cannot create the file inside a directory that does not exist.
    url = f"sqlite:///{tmp_path / 'missing' / 'database.db'}"
    with TestClient(create_app(url)) as client:
        assert client.get("/health").json() == {"status": "ok"}
        assert client.get("/health").status_code == 200
        response = client.get("/api/projects")
        assert response.status_code == 503
        assert response.json() == {"detail": "Banco de dados indisponível."}
        response = client.post("/api/projects", json={"title": "Painel", "customer": "Teste"})
        assert response.status_code == 503
        assert (
            "503"
            in client.get("/openapi.json").json()["paths"]["/api/projects"]["get"]["responses"]
        )

    (tmp_path / "missing").mkdir()
    with TestClient(create_app(url)) as client:
        assert client.get("/api/projects").json() == []


def test_healthcheck_is_liveness_and_does_not_access_database(client):
    with patch.object(
        client.app.state, "session_factory", side_effect=AssertionError("Banco usado")
    ):
        response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "ok"}


def test_health_and_business_errors_have_openapi_contract(client):
    spec = client.get("/openapi.json").json()
    health = spec["paths"]["/health"]["get"]["responses"]["200"]
    assert health["content"]["application/json"]["schema"]["$ref"].endswith("/HealthRead")
    errors = spec["paths"]["/api/projects/{project_id}"]["delete"]["responses"]
    for code in ("404", "409"):
        assert errors[code]["content"]["application/json"]["schema"]["$ref"].endswith(
            "/ErrorResponse"
        )
    assert "422" in spec["paths"]["/api/projects"]["post"]["responses"]


def test_missing_project_response_matches_documented_error(client):
    response = client.get("/api/projects/999")
    assert response.status_code == 404
    assert ErrorResponse.model_validate(response.json()).detail == "Projeto não encontrado."
