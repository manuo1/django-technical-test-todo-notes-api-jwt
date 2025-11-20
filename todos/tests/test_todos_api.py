# todos/tests/test_api.py
import pytest

from notes.models import Note
from todos.models import Todo


@pytest.mark.django_db
def test_list_todos_returns_200(api_client_authenticated):
    response = api_client_authenticated.get("/api/todos/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_todo(api_client_authenticated):
    data = {"title": "Ma première tâche", "status": "pending"}
    response = api_client_authenticated.post("/api/todos/", data)
    assert response.status_code == 201
    assert response.json()["title"] == "Ma première tâche"
    assert response.json()["status"] == "pending"
    assert Todo.objects.count() == 1


@pytest.mark.django_db
def test_create_todo_with_note(api_client_authenticated):
    note = Note.objects.create(text="Note associée")
    data = {"title": "Tâche avec note", "status": "pending", "note": note.id}
    response = api_client_authenticated.post("/api/todos/", data)
    assert response.status_code == 201
    assert response.json()["note"] == note.id


@pytest.mark.django_db
def test_retrieve_todo(api_client_authenticated):
    todo = Todo.objects.create(title="Test todo", status="pending")
    response = api_client_authenticated.get(f"/api/todos/{todo.id}/")
    assert response.status_code == 200
    assert response.json()["title"] == "Test todo"


@pytest.mark.django_db
def test_update_todo(api_client_authenticated):
    todo = Todo.objects.create(title="Ancienne tâche", status="pending")
    data = {"title": "Tâche mise à jour", "status": "done"}
    response = api_client_authenticated.put(f"/api/todos/{todo.id}/", data)
    assert response.status_code == 200
    assert response.json()["title"] == "Tâche mise à jour"
    assert response.json()["status"] == "done"


@pytest.mark.django_db
def test_partial_update_todo(api_client_authenticated):
    todo = Todo.objects.create(title="Tâche originale", status="pending")
    data = {"status": "in_progress"}
    response = api_client_authenticated.patch(f"/api/todos/{todo.id}/", data)
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"
    assert response.json()["title"] == "Tâche originale"


@pytest.mark.django_db
def test_delete_todo(api_client_authenticated):
    todo = Todo.objects.create(title="À supprimer", status="pending")
    response = api_client_authenticated.delete(f"/api/todos/{todo.id}/")
    assert response.status_code == 204
    assert Todo.objects.count() == 0


@pytest.mark.django_db
def test_list_todos_without_auth_returns_401(api_client):
    response = api_client.get("/api/todos/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_todo_without_title_returns_400(api_client_authenticated):
    response = api_client_authenticated.post("/api/todos/", {})
    assert response.status_code == 400


@pytest.mark.django_db
def test_retrieve_nonexistent_todo_returns_404(api_client_authenticated):
    response = api_client_authenticated.get("/api/todos/999/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_list_todos_returns_all_todos(api_client_authenticated):
    Todo.objects.create(title="Todo 1", status="pending")
    Todo.objects.create(title="Todo 2", status="done")
    response = api_client_authenticated.get("/api/todos/")
    assert len(response.json()) == 2
