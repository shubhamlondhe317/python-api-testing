import pytest

from lib.utils import load_params

student_technical_details = load_params("student_technical_details.yaml")
print(student_technical_details)


@pytest.mark.SVT
@pytest.mark.parametrize(
    "test_params",
    student_technical_details,
    ids=[x["id"] for x in student_technical_details],
)
def test_get_technical_student_details(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.get(base_url + "/api/technicalskills")
    print(response.text)
    assert response.status_code == 200


@pytest.mark.SVT
@pytest.mark.parametrize(
    "test_params",
    student_technical_details,
    ids=[x["id"] for x in student_technical_details],
)
def test_technical_student_details(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.post(base_url + "/api/technicalskills", test_params)
    print(response.text)
    assert response.status_code == 200
