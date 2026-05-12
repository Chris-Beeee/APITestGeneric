#test will fail intentionally as post 0 does not exist
import pytest

@pytest.mark.xfail(
    reason="Intentionally failing because post 0 does not exist, so it returns an empty list of comments")
def test_get_comments_for_invalid_post(api_client):
    # Pass the nested route directly into api_client.get()
    response = api_client.get("/posts/0/comments")

    # This assertion actually passes because the API returns 200 OK
    assert response.status_code == 200

    data = response.json()

    # The assertion fails here, triggering the expected failure,
    # because the empty list [] has a length of 0.
    assert len(data) > 0

    for comment in data:
        assert comment["postId"] == 0