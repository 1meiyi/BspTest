import requests
import re
import json
import base64
from requests.utils import dict_from_cookiejar

gr_umd_url = 'Z3ItdW1kL3JlbGVhc2VfTTEwMDBfMS4yLjAv'  # gr-umd/release_M1000_1.2.0/


class Autoinstall:
    def __init__(self):
        self.payload = json.dumps({
            "accessKey": "mtoss",
            "secretKey": "mtoss123"
        })
        try:
            self.session = requests.session()
        except TimeoutError:
            print('连接服务器超时')
        self.url = 'https://oss.mthreads.com:9001/api/v1/'
        self.buckets = 'buckets/'

    def get_headers(self):

        return {
            'Content-Type': 'application/json',
            'Cookie': f"token={self.token}",
        }

    def get_session(self):
        print('登录')
        path = 'login'
        headers = {
            'Content-Type': 'application/json'
        }
        for i in range(5):
            res = self.session.post(url=self.url + path, data=self.payload, headers=headers, timeout=15)
            print("状态码:", res.status_code)
            if res.status_code == 201:
                try:
                    self.token = dict_from_cookiejar(res.cookies)['token']
                    return self.token
                except TimeoutError:
                    print('连接超时，无法获取token')
                print("状态码:", res.status_code)

            else:
                print(f'第{i + 1}次尝试连接')
                continue

    def get_gr_umd(self):
        print('umd仓库')
        headers = self.get_headers()
        path = self.prefix('gr-umd/release_M1000_1.2.0')
        print(path, 'path')

        # https://oss.mthreads.com:9001/api/v1/buckets/release-ci/objects?prefix = Z3ItdW1kL3JlbGVhc2VfTTEwMDBfMS4yLjAv
        response = self.session.get(f'{self.url}{self.buckets}release-ci/objects?prefix={path}', headers=headers)
        print(response.status_code)
        print(response.json(), 'gr-umd')

    def get_buckets(self):
        print('仓库')
        headers = self.get_headers()
        response = self.session.get(f'{self.url}{self.buckets}', headers=headers)
        print(response.status_code)
        res =json.dumps(response.json())
        print(res)


    def list_file(self):
        headers = self.get_headers()
        response = self.session.get(f'{self.url}{self.buckets}', headers=headers)
        print(response.status_code)
        print(response.json())

    def prefix(self, path):
        prefix = base64.b64encode(path.encode()).decode()
        return prefix


if __name__ == '__main__':
    # https://oss.mthreads.com:9001/api/v1/buckets/release-ci/objects?prefix=Z3ItdW1kL3JlbGVhc2VfTTEwMDBfMS4yLjAv
    fp = Autoinstall()
    fp.get_session()
    fp.get_buckets()
    fp.get_gr_umd()
