def test_get_comments_for_post(api_client):
    # Pass the nested route directly into api_client.get()
    response = api_client.get("/posts/1/comments")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for comment in data:
        assert comment["postId"] == 1