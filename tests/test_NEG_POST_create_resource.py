import pytest


@pytest.mark.xfail(
    reason="Intentionally failing because sending a POST to the non-existent /post endpoint returns a 404")
def test_create_post_invalid_endpoint(api_client):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # This will return a 404 Not Found instead of 201 Created
    response = api_client.post("/post", json=payload)

    # Assertion fails
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == 101  # JSONPlaceholder assigns ID 101 to new posts