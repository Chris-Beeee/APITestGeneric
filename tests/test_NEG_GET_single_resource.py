#test will fail intentionally because /post does not exist
import pytest


@pytest.mark.xfail(reason="Intentionally failing because the endpoint /post/ does not exist")
def test_get_single_post_invalid_endpoint(api_client):
    # This will return a 404 Not Found
    response = api_client.get("/post/")

    # The assertion fails here, triggering the expected failure
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    assert isinstance(data["title"], str)