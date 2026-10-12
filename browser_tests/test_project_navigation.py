import pytest
from playwright.sync_api import expect


def create_project(page, url, title, task):
    response = page.request.post(
        f"{url}/api/projects", data={"title": title, "customer": "Cliente fictício"}
    )
    assert response.status == 201
    project_id = response.json()["id"]
    response = page.request.post(f"{url}/api/projects/{project_id}/tasks", data={"title": task})
    assert response.status == 201


@pytest.mark.parametrize("width", [1440, 390])
def test_click_selected_project_opens_its_details(page, live_url, width):
    create_project(page, live_url, "Painel de teste", "Conferir componentes")
    page.set_viewport_size({"width": width, "height": 800})
    page.goto(live_url)
    card = page.locator(".project-card")
    expect(card).to_have_attribute("aria-pressed", "true")
    card.get_by_text("Painel de teste", exact=True).click()
    heading = page.locator("#project-title")
    expect(heading).to_be_focused()
    expect(heading).to_be_in_viewport()
    expect(page.locator(".task-title")).to_have_text("Conferir componentes")


def test_switch_project_shows_only_its_tasks_and_clears_filter(page, live_url):
    create_project(page, live_url, "Projeto A", "Tarefa A")
    create_project(page, live_url, "Projeto B", "Tarefa B")
    page.goto(live_url)
    expect(page.locator("#project-title")).to_have_text("Projeto B")
    page.locator("#status-filter").select_option("done")
    expect(page.locator(".task-title")).to_have_count(0)
    card = page.locator(".project-card").filter(has_text="Projeto A")
    card.focus()
    page.keyboard.press("Enter")
    expect(page.locator("#project-title")).to_have_text("Projeto A")
    expect(page.locator("#project-title")).to_be_focused()
    expect(page.locator("#status-filter")).to_have_value("")
    expect(page.locator(".task-title")).to_have_text("Tarefa A")


def test_project_status_follows_task_execution(page, live_url):
    create_project(page, live_url, "Projeto de montagem", "Montar painel")
    page.goto(live_url)
    expect(page.locator(".status-help")).to_contain_text("Status automático")
    expect(page.locator("#project-status")).to_have_text("Pendente")
    task_status = page.get_by_label("Status de Montar painel", exact=True)
    task_status.select_option("in_progress")
    expect(page.locator("#project-status")).to_have_text("Em andamento")
    task_status.select_option("done")
    expect(page.locator("#project-status")).to_have_text("Concluído")
    expect(page.locator("#progress")).to_have_attribute("value", "100")
    task_status.select_option("pending")
    expect(page.locator("#project-status")).to_have_text("Pendente")
