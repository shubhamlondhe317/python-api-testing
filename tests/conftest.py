import pytest
import requests


@pytest.fixture(scope="session")
def start_executions():
    return requests.Session()
