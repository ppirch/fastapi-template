from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    expect_response = {"msg": "FastAPI", "version": "0.1"}
    assert response.status_code == 200
    assert response.json() == expect_response
