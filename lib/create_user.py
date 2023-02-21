import requests

payload ={
    "name": "morpheus",
    "job" : "Automation"
}

resp=requests.post("https://reqres.in/api/users",data=payload)
print(resp)
assert resp.status_code==201
print(resp.json())
