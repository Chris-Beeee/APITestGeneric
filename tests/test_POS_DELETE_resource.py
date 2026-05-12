def test_delete_post(api_client):
    # Use api_client.delete() and pass just the endpoint route
    response = api_client.delete("/posts/1")
    # JSONPlaceholder typically returns 200 OK for successful deletes
    assert response.status_code == 200
    assert response.json() == {}  # Returns an empty object