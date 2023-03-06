import json

import jsonpath
import pytest
import requests

# API URL
url = "https://reqres.in/api/users"

a=11
@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open("/Users/shubhamlondhe/Downloads/CreateUser.json", "r")

@pytest.mark.Regression
def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make Post request with json input body
    response = requests.post(url, request_json)
    # VAlidating response code
    assert response.status_code ==201
    # Fetch header from response
    # print(response.headers.get('Content-length'))
    # # Parse response to json format
    # response_json = json.loads(response.text)
    # # Pick id using json path
    # id = jsonpath.jsonpath(response_json,'id')
    # print(id[0])

@pytest.mark.SVT
def test_create_other_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make Post request with json input body
    response = requests.post(url, request_json)
    # VAlidating response code
    # assert response.status_code ==201
    # Fetch header from response
    # print(response.headers.get('Content-length'))
    # Parse response to json format
    response_json = json.loads(response.text)
    # Pick id using json path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])