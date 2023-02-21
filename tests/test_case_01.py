import pytest

actual_result = "Hello"

@pytest.mark.Smoke
def test_login_logout_testing():
    print("This is first smoke test case")
    print("This is end of test....")
    assert actual_result != "Hello"

@pytest.mark.Sanity
def test_login_logout_invalid_credentials():
    print("This is Sanity invalid test")
    print("end invalid testcase.")