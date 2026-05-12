def test_get_all_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100  # returns 100 posts