from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo API is running"}

def test_create_and_get_todo():
    todo_data = {"id": 1, "title": "Test Todo"}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 200
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "Test Todo"