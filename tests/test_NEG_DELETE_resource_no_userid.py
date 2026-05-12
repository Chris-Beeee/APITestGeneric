import pytest


# indicates expected failure as this is a negative test case
@pytest.mark.xfail(reason="PostID does not exist, but JSONPlaceholder incorrectly returns 200 OK")
def test_delete_non_existent_post(api_client):
    response = api_client.delete("/posts/123123123123")

  #asserts failure response correctly. The API incorrectly returns a 200 error
    assert response.status_code == 404