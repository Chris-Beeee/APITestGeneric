def test_get_single_post(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    assert isinstance(data["title"], str)