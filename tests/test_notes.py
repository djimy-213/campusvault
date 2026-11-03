from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_then_read():
    r = client.post("/notes", json={"title": "Docker", "body": "namespaces + cgroups"})
    assert r.status_code == 201
    note_id = r.json()["id"]
    assert r.headers["Location"] == f"/notes/{note_id}"
    assert client.get(f"/notes/{note_id}").json()["title"] == "Docker"


def test_missing_note_is_404():
    assert client.get("/notes/99999").status_code == 404


def test_unknown_field_is_rejected():
    r = client.post("/notes", json={"title": "x", "owner": "admin"})
    assert r.status_code == 422


def test_title_too_long_is_rejected():
    r = client.post("/notes", json={"title": "a" * 101})
    assert r.status_code == 422


def test_delete_then_404():
    r = client.post("/notes", json={"title": "temp"})
    note_id = r.json()["id"]
    assert client.delete(f"/notes/{note_id}").status_code == 204
    assert client.get(f"/notes/{note_id}").status_code == 404
