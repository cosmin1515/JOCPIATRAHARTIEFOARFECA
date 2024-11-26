from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_user_create():
    response = client.post("/user_create", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"
