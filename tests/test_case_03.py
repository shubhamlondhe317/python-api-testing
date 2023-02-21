import pytest

@pytest.fixture(scope="module")
def fixture_code():
    print("This will execute before testcase")
    print("-----------------------------------")
    yield
    print("close DB connection after executing testcase")
    print("-----------------------------------")

@pytest.mark.Smoke
def test_login_logout_testing(fixture_code):
    print("This is first test case")
    print("This is end of test....")

@pytest.mark.Sanity
def test_login_logout_invalid_credentials(fixture_code):
    print("This is invalid test")
    print("end invalid testcase.")