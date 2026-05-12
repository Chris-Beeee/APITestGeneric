import pytest

#test will fail intentionally as userid does not exist
@pytest.mark.xfail(reason="Intentionally failing because userId 9999 does not exist and returns an empty list")
def test_filter_posts_by_userid(api_client):
    # Pass a userId that does not exist
    response = api_client.get("/posts", params={"userId": ""})

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0
    # Ensure every returned post belongs to userId 1
    for post in data:
        assert post["userId"] == 1