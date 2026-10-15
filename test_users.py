import os
import uuid
import requests

BASE_URL = "http://localhost:8000"


def test_create_user():
    payload = {
        "name": "Pytest User",
        "email": f"{uuid.uuid4().hex}@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=5
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data


def test_get_user_created_by_postman():
    # Set POSTMAN_USER_ID to the ID returned by Postman.
    user_id = os.environ.get("POSTMAN_USER_ID")

    if not user_id:
        import pytest
        pytest.skip("Set POSTMAN_USER_ID to a Postman-created user ID")

    response = requests.get(
        f"{BASE_URL}/users/{int(user_id)}",
        timeout=5
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == int(user_id)
    assert data["name"] == "Alice"
    assert data["email"] == "alice.demo@example.com"