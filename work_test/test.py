import requests
import json
from requests.auth import HTTPBasicAuth
from requests.utils import dict_from_cookiejar

payload = json.dumps({
    "accessKey": "mtoss",
    "secretKey": "mtoss123"
})
headers = {
    'Content-Type': 'application/json'
}
url = 'https://oss.mthreads.com:9001/api/v1/login'
session = requests.session()
# data = bytes(payload, encoding='utf8')
response = session.post(url, data=payload, headers=headers)


# print(session.cookies.get_dict(), '###############################################')
cookies_dict = dict_from_cookiejar(response.cookies)
print(cookies_dict,'**********************************')
print(response.status_code)
for i in range(5):
    if response.status_code == 201:
        print(response.status_code)
        print(response.headers)
        print(response.cookies)
        break
    else:
        print(f'第{i + 1}次尝试连接')
        continue

