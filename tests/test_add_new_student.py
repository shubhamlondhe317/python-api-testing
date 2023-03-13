import pytest

from tests.test_end_to_end import student_details


@pytest.mark.BVT
@pytest.mark.parametrize(
    "test_params",
    student_details,
    ids=[x["id"] for x in student_details],
)
def test_get_student_data(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.get(base_url + "/api/studentsDetails/7081053")
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.Regressions
@pytest.mark.parametrize(
    "test_params",
    student_details,
    ids=[x["id"] for x in student_details],
)
def test_add_new_student(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.post(base_url + "/api/studentsDetails", test_params)
    print(response.text)
    assert response.status_code == 201


@pytest.mark.SVT
@pytest.mark.parametrize(
    "test_params",
    student_details,
    ids=[x["id"] for x in student_details],
)
def test_update_new_student(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.put(base_url+"/api/studentsDetails/7081054", test_params)
    print(response.text)
