import pytest


@pytest.mark.Smoke
def test_login_logout_testing():
    print("This is first test case")
    print("This is end of test....")

@pytest.mark.Sanity
def test_login_logout_invalid_credentials():
    print("This is invalid test")
    print("end invalid testcase.")