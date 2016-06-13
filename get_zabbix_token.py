#-*- coding:utf-8-*-

import requests
import json

header = {"Content-Type": "application/json"}

payload = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "admin",
        "password": "xxoo"
    },
    "id": 1,
    "auth": None
})

url = "http://xxx.xxx.com/api_jsonrpc.php"

r = requests.post(url, data=payload, headers=header)
result = json.loads(r.text)
print(result)
