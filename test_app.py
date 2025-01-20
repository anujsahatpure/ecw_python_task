import pytest
from app import app, tasks  # Import tasks to reset it

@pytest.fixture
def client():
    # Reset tasks list before every test
    tasks.clear()
    app.testing = True
    return app.test_client()

def test_get_tasks(client):
    # Test the GET /tasks route
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []

def test_add_task(client):
    # Test the POST /tasks route
    new_task = {"task": "Buy groceries"}
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    assert response.json["task"] == "Buy groceries"
    assert response.json["done"] is False

def test_add_task_invalid(client):
    # Test POST /tasks route with invalid data (empty task)
    response = client.post('/tasks', json={"task": ""})
    assert response.status_code == 400
    assert response.json == {"error": "Task cannot be empty"}

def test_update_task(client):
    # First, add a task
    response = client.post('/tasks', json={"task": "Buy milk"})
    task_id = response.json["id"]

    # Then, update that task
    updated_task = {"task": "Buy milk and eggs", "done": True}
    response = client.put(f'/tasks/{task_id}', json=updated_task)
    assert response.status_code == 200
    assert response.json["task"] == "Buy milk and eggs"
    assert response.json["done"] is True

def test_mark_task_done(client):
    # First, add a task
    response = client.post('/tasks', json={"task": "Do laundry"})
    task_id = response.json["id"]

    # Mark the task as done
    response = client.put(f'/tasks/{task_id}/done')
    assert response.status_code == 200
    assert response.json["done"] is True

def test_delete_task(client):
    # First, add a task
    response = client.post('/tasks', json={"task": "Go jogging"})
    task_id = response.json["id"]

    # Delete the task
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.json == {"message": "Task deleted"}

    # Ensure the task is deleted
    response = client.get('/tasks')
    assert len(response.json) == 0  # Task list should be empty after deletion
