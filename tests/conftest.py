import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """
    Returns an instance of APIClient to be used across all tests.
    Session scope means it's created once per test run.
    """
    client = APIClient()
    return client
