import pytest
import time

# --- Example 1: Data-Driven Testing using @pytest.mark.parametrize ---
# This allows you to run the same test function multiple times with different inputs.
@pytest.mark.parametrize("post_id, expected_title", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
    (2, "qui est esse"),
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),
])
def test_get_post_by_id(api_client, post_id, expected_title):
    """Test fetching specific posts and validating their titles."""
    response = api_client.get(f"/posts/{post_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert data["title"] == expected_title


# --- Example 2: Testing Error Status Codes ---
# It's important to verify how your API handles bad requests or missing resources.
def test_get_non_existent_resource(api_client):
    """Test requesting a resource that doesn't exist returns 404."""
    response = api_client.get("/posts/999999")
    
    # jsonplaceholder returns 404 for missing items
    assert response.status_code == 404


# --- Example 3: Performance/Timeout Testing ---
# Validating that an API responds within a reasonable amount of time.
def test_api_response_time(api_client):
    """Test that the /comments endpoint responds within 1 second."""
    start_time = time.time()
    response = api_client.get("/comments")
    end_time = time.time()
    
    duration = end_time - start_time
    assert response.status_code == 200
    assert duration < 1.0, f"API took too long: {duration} seconds"


# --- Example 4: Full CRUD Lifecycle ---
# Validating Create, Read, Update, and Delete in a single cohesive flow.
def test_post_crud_lifecycle(api_client):
    """Test the full lifecycle of a Post resource."""
    # 1. CREATE
    payload = {"title": "My New Post", "body": "This is the content.", "userId": 1}
    create_resp = api_client.post("/posts", json=payload)
    assert create_resp.status_code == 201
    created_post = create_resp.json()
    post_id = created_post["id"]
    
    assert created_post["title"] == "My New Post"

    # NOTE: jsonplaceholder fakes POST/PUT/DELETE, so the resource isn't *actually* saved on their server.
    # In a real API, you would do a GET here to verify it was saved.
    # get_resp = api_client.get(f"/posts/{post_id}")
    # assert get_resp.status_code == 200
    
    # 2. UPDATE (PUT)
    update_payload = {"id": post_id, "title": "Updated Title", "body": "Updated content.", "userId": 1}
    # We'll use ID 1 for the PUT request since jsonplaceholder expects an existing ID to mock a PUT
    update_resp = api_client.put("/posts/1", json=update_payload)
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated Title"

    # 3. DELETE
    delete_resp = api_client.delete("/posts/1")
    assert delete_resp.status_code == 200


# --- Example 5: Validating Response Schema ---
# While you can use libraries like `jsonschema`, you can also do basic type checking natively.
def test_response_schema_types(api_client):
    """Test that the response payload matches the expected data types."""
    response = api_client.get("/todos/1")
    assert response.status_code == 200
    
    data = response.json()
    
    # Basic schema validation
    expected_keys = {"userId", "id", "title", "completed"}
    assert set(data.keys()) == expected_keys
    
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["completed"], bool)


# --- Example 6: Testing Query Parameters ---
def test_query_parameters(api_client):
    """Test passing query parameters to filter results."""
    # This will send a request to /comments?postId=1
    # requests library handles urlencoding the 'params' dictionary automatically
    response = api_client.get("/comments", params={"postId": 1})
    
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) > 0
    # Verify all returned comments actually belong to postId 1
    for comment in data:
        assert comment["postId"] == 1
