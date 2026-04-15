import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello, Flask!"

def test_add(client):
    resp = client.get("/add/2/3")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5