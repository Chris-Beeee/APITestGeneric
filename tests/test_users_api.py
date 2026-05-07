def test_get_users(api_client):
    """Test retrieving a list of users."""
    response = api_client.get("/users")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]

def test_create_user(api_client):
    """Test creating a new user."""
    payload = {
        "name": "Jane Doe",
        "username": "janedoe",
        "email": "jane@example.com"
    }
    response = api_client.post("/users", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert "id" in data

def test_delete_user(api_client):
    """Test deleting an existing user."""
    response = api_client.delete("/users/2")
    
    # jsonplaceholder returns 200 for successful deletion
    assert response.status_code == 200
