import json

import jsonpath


def test_add_new_student(start_executions):
    file = open("/Users/shubhamlondhe/Documents/requestJson.json", "r")
    json_request = json.loads(file.read())
    response = start_executions.post("https://thetestingworldapi.com/api/studentsDetails", json_request)
    print(response.text)
    assert response.status_code == 201
    assert response.json()["first_name"] == "Testing"


def test_update_new_student(start_executions):
    file = open("/Users/shubhamlondhe/Documents/requestJson.json", "r")
    json_request = json.loads(file.read())
    response = start_executions.put("https://thetestingworldapi.com/api/studentsDetails/7081053", json_request)
    assert response.status_code == 404
    print(response.text)


# def test_delete_student():
#     api_url = "https://thetestingworldapi.com/api/studentsDetails/7081053"
#     response = requests.delete(api_url)
#     assert response.text == "No data Found"
#     print(response.text)

def test_get_student_data(start_executions):
    response = start_executions.get("https://thetestingworldapi.com/api/studentsDetails/7081054")
    json_response = json.loads(response.text)  # response.json
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 7081054
