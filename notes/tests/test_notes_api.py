import pytest

from notes.models import Note


@pytest.mark.django_db
def test_list_notes_without_auth_returns_401(api_client):
    response = api_client.get("/api/notes/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_list_notes_returns_200(api_client_authenticated):
    response = api_client_authenticated.get("/api/notes/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_note(api_client_authenticated):
    data = {"text": "Ma première note"}
    response = api_client_authenticated.post("/api/notes/", data)
    assert response.status_code == 201
    assert response.json()["text"] == "Ma première note"
    assert Note.objects.count() == 1


@pytest.mark.django_db
def test_retrieve_note(api_client_authenticated):
    note = Note.objects.create(text="Test note")
    response = api_client_authenticated.get(f"/api/notes/{note.id}/")
    assert response.status_code == 200
    assert response.json()["text"] == "Test note"


@pytest.mark.django_db
def test_update_note(api_client_authenticated):
    note = Note.objects.create(text="Ancienne note")
    data = {"text": "Note mise à jour"}
    response = api_client_authenticated.put(f"/api/notes/{note.id}/", data)
    assert response.status_code == 200
    assert response.json()["text"] == "Note mise à jour"


@pytest.mark.django_db
def test_partial_update_note(api_client_authenticated):
    note = Note.objects.create(text="Note originale")
    data = {"text": "Note modifiée"}
    response = api_client_authenticated.patch(f"/api/notes/{note.id}/", data)
    assert response.status_code == 200
    assert response.json()["text"] == "Note modifiée"


@pytest.mark.django_db
def test_delete_note(api_client_authenticated):
    note = Note.objects.create(text="À supprimer")
    response = api_client_authenticated.delete(f"/api/notes/{note.id}/")
    assert response.status_code == 204
    assert Note.objects.count() == 0


@pytest.mark.django_db
def test_create_note_without_text_returns_400(api_client_authenticated):
    response = api_client_authenticated.post("/api/notes/", {})
    assert response.status_code == 400


@pytest.mark.django_db
def test_retrieve_nonexistent_note_returns_404(api_client_authenticated):
    response = api_client_authenticated.get("/api/notes/999/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_list_notes_returns_all_notes(api_client_authenticated):
    Note.objects.create(text="Note 1")
    Note.objects.create(text="Note 2")
    response = api_client_authenticated.get("/api/notes/")
    assert len(response.json()) == 2
