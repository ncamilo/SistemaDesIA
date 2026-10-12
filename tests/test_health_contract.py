from unittest.mock import patch

from app.schemas import ErrorResponse


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
