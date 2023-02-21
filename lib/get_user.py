import requests

p={"page":2}
resp = requests.get("https://reqres.in/api/users?",params=p)
print(resp.url)
json_response = resp.json()
print(type(resp))
print(resp)
assert resp.status_code == 200, "response is not matching."
print(json_response['total'])

print(json_response['total_pages'])
print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in")

