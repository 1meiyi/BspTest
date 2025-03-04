import requests
import re
import json
import base64
from requests.utils import dict_from_cookiejar
import datetime
from BspTest.Utils import Base_init

class Autoinstall:
    def __init__(self):
        self.payload = json.dumps({
            "accessKey": "mtoss",
            "secretKey": "mtoss123"
        })
        try:
            self.requests = requests.session()
        except requests.exceptions.ReadTimeout:
            print('连接服务器超时')
        self.url = 'https://oss.mthreads.com:9001/api/v1/'
        self.buckets = 'buckets/'

    def get_headers(self):

        return {
            'Content-Type': 'application/json',
            'Cookie': f"token={self.token}",
        }

    def get_session(self):
        path = 'login'
        headers = {
            'Content-Type': 'application/json'}
        for i in range(5):

            try:
                print(f'第{i + 1}次尝试获取session id')
                res = self.requests.post(url=self.url + path, data=self.payload, headers=headers, timeout=15)
                print(res.status_code)
                if f'{res.status_code}'.startswith('2'):
                    self.token = dict_from_cookiejar(res.cookies)['token']
                    print('成功获取session id')
                    return self.token
                else:
                    print(f'第{i + 1}次尝试连接')
                    continue
            except requests.exceptions.ReadTimeout:
                print('连接超时，无法获取token')

    def get_gr_umd(self):
        print('umd仓库')
        path = self.enbase('gr-umd/release_M1000_1.2.0')
        # https://oss.mthreads.com:9001/api/v1/buckets/release-ci/objects?prefix = Z3ItdW1kL3JlbGVhc2VfTTEwMDBfMS4yLjAv
        response = self.requests.get(f'{self.url}{self.buckets}release-ci/objects?prefix={path}',
                                     headers=self.get_headers())
        print(response.status_code)
        print(response.text)
        print(response.json(), 'gr-umd')

    def get_buckets(self):
        print('仓库')
        response = self.requests.get(f'{self.url}{self.buckets}')
        print(response.status_code)

    def get_GPU_driver(self):
        # timedate = datetime.date.today().strftime('%Y%m%d')
        timedate = '20250206'
        prefix = self.enbase(f'release_M1000_1.2.0/{timedate}')
        # prefix = {prefix}
        url = f'{self.url}{self.buckets}product-release/objects?prefix={prefix}'
        print(url)
        response = self.requests.get(url, headers=self.get_headers())
        print(response.status_code)
        print(response.text)

    def get_kenels(self):
        # timedate = datetime.date.today().strftime('%Y%m%d')
        deb_name = []
        prefix = self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/')
        master_url = f'{self.url}{self.buckets}sw-build/objects?prefix={prefix}'
        res_date = self.requests.get(master_url, headers=self.get_headers())
        timedate = [re.search('[0-9]{8}', i['name']).group() for i in res_date.json()['objects'] if
                    re.search('[0-9]{8}', i['name']).group()]
        deb_prefix = self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/{timedate[-1]}/kernel-debs/')
        deb_url = f'{self.url}{self.buckets}sw-build/objects?prefix={deb_prefix}'
        deb_res = requests.get(deb_url,headers=self.get_headers())
        for i in range(5):
            deb_name.append(deb_res.json()['objects'][i]['name'])
        for j in deb_name:
            if j.endswith('.deb'):
                print(f'wget https://oss.mthreads.com/sw-build/{j}')
                pass  # 执行下载

    def list_file(self):
        response = self.requests.get(f'{self.url}{self.buckets}')
        print(response)

    def enbase(self, path):
        prefix = base64.b64encode(path.encode()).decode()
        return prefix

    def debase(self, path):
        prefix = base64.b64decode(path.encode()).decode()
        return prefix


if __name__ == '__main__':
    # https://oss.mthreads.com:9001/api/v1/buckets/release-ci/objects?prefix=Z3ItdW1kL3JlbGVhc2VfTTEwMDBfMS4yLjAv
    fp = Autoinstall()
    fp.get_session()
    fp.get_kenels()
    # fp.get_buckets()
    # fp.get_gr_umd()
