from urllib.parse import urlencode
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_template():
    path = "/template?"
    query = {}
    response = client.get(path + urlencode(query))
    expect_response = {"res": "example text"}
    assert response.status_code == 200
    assert response.json() == expect_response


def test_get_template_with_query():
    path = "/template?"
    query = {"text": "query"}
    response = client.get(path + urlencode(query))
    expect_response = {"res": "query"}
    assert response.status_code == 200
    assert response.json() == expect_response
