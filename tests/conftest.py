import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(f"sqlite:///{tmp_path / 'test.db'}")
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def project(client):
    response = client.post("/api/projects", json={"title": "Painel", "customer": "Cliente exemplo"})
    assert response.status_code == 201
    return response.json()
