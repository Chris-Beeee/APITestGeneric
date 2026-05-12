#Test will fail intentionally because /post does not exist, /posts does
import pytest

@pytest.mark.xfail(reason="Intentionally calling a non-existent endpoint (/post instead of /posts)")
def test_get_all_posts_invalid_endpoint(api_client):
    # Returns 404 Not Found
    response = api_client.get("/post")

    # Compares status and rejects the incorrect response
    assert response.status_code == 200

    # Test has already failed
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100