import jsonpath
import pytest

from lib.utils import load_params

student_details = load_params("student_details.yaml")
print(student_details)
print("************")


@pytest.mark.BVT
@pytest.mark.parametrize(
    "test_params",
    student_details,
    ids=[x["id"] for x in student_details],
)
def test_add_new_data(start_executions, test_params, base_url):
    print(test_params)
    response = start_executions.post(base_url+"/api/studentsDetails", test_params)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])
    assert response.status_code == 201




