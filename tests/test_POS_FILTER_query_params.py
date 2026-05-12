def test_filter_posts_by_userid(api_client):
    response = api_client.get("/posts", params={"userId": 1})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

    # Ensure every returned post belongs to userId 1
    for post in data:
        assert post["userId"] == 1