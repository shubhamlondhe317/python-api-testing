import pytest
import requests


@pytest.fixture(scope="session")
def start_executions():
    return requests.Session()


@pytest.fixture(scope="session")
def api_url():
    return "https://thetestingworldapi.com"
