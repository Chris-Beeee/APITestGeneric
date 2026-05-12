def test_create_post(api_client):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == 101  # JSONPlaceholder assigns ID 101 to new posts