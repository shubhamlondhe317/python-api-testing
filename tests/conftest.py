import pytest
import requests


@pytest.fixture(scope="session")
def start_executions():
    return requests.Session()


def pytest_addoption(parser):
    parser.addoption('--host', action='store', default="https://thetestingworldapi.com",
                     help='Base URL for the API tests')


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption('--host')
