def test_update_post_put(api_client):
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    # Use api_client.put() and pass just the endpoint route
    response = api_client.put("/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"