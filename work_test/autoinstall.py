import requests
import re
import json
import base64
from requests.utils import dict_from_cookiejar
import roll_back
import Base_init

pc = Base_init.BspTest()


class Autoinstall:
    def __init__(self):
        # 定义payload
        self.payload = json.dumps({
            "accessKey": "mtoss",
            "secretKey": "mtoss123"
        })
        try:
            # 初始化句柄
            self.requests = requests.session()
        except requests.exceptions.ReadTimeout:
            print('连接服务器超时')
        self.url = 'https://oss.mthreads.com:9001/api/v1/'
        self.buckets = 'buckets/'

    def get_headers(self):
        # 定义全局headers
        return {
            'Content-Type': 'application/json',
            'Cookie': f"token={self.token}",
        }

    def get_session(self):
        path = 'login'
        # 定义header
        headers = {
            'Content-Type': 'application/json'}
        for i in range(5):
            try:
                print(f'第{i + 1}次尝试获取session id')
                # 请求网址返回session id
                res = self.requests.post(url=self.url + path, data=self.payload, headers=headers, timeout=15)
                print(res.status_code)
                if f'{res.status_code}'.startswith('2'):
                    try:
                        # 获取并返回token
                        self.token = dict_from_cookiejar(res.cookies)['token']
                        print('成功获取session id')
                        return self.token
                    except AttributeError:
                        print('服务器超时')
                else:
                    print(f'第{i + 1}次尝试连接')
                    continue
            except requests.exceptions.ReadTimeout:
                print('连接超时，无法获取token')

    def get_gr_umd(self):
        path = self.enbase('gr-umd/release_M1000_1.2.0/')
        res = self.requests.get(f'{self.url}{self.buckets}release-ci/objects?prefix={path}',
                                headers=self.get_headers())
        # 获取commit id 与 架构 拼接字符串
        deb_url = [i['name'] for i in res.json()['objects'] if
                   i['name'].endswith(
                       f'{roll_back.choose_download()}_{roll_back.ger_frame_text()}-mtgpu_linux-xorg-release-hw-glvnd.tar.gz')]
        print(deb_url)
        # 下载deb 包
        print(f'wget https://oss.mthreads.com/release-ci/gr-umd/release_M1000_1.2.0/{deb_url}')

    def get_buckets(self):
        print('仓库')
        response = self.requests.get(f'{self.url}{self.buckets}')
        print(response.status_code)

    def get_gpu_driver(self):
        # timedate = datetime.date.today().strftime('%Y%m%d')
        # 编码仓库地址
        prefix = self.enbase('release_M1000_1.2.0/')
        # 拼接 url
        url = f'{self.url}{self.buckets}product-release/objects?prefix={prefix}'
        # 根据时间获取最新仓库
        time_date = [i['name'] for i in self.requests.get(url, headers=self.get_headers()).json()['objects']]
        deb_url = f'{self.url}{self.buckets}product-release/objects?prefix={self.enbase(f'{time_date[-1]}')}'
        # 筛选deb
        deb_name = [i['name'] for i in self.requests.get(deb_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.deb')]
        # 循环遍历下载
        for deb in deb_name:
            if deb.endswith('.deb'):
                print(f'wget https://oss.mthreads.com/{deb} -P ./daily/gpu')
                pass  # 执行下载

    def get_kernels(self):
        # timedate = datetime.date.today().strftime('%Y%m%d')
        # 编码kernel prefix
        prefix = self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/')
        # 拼接仓库日期Url
        master_url = f'{self.url}{self.buckets}sw-build/objects?prefix={prefix}'
        # 获取仓库日期
        time_date = [i['name'] for i in self.requests.get(master_url, headers=self.get_headers()).json()['objects']]
        # 拼接deb包 Url
        deb_url = f'{self.url}{self.buckets}sw-build/objects?prefix={self.enbase(f'{time_date[-1]}kernel-debs/')}'
        # 筛选deb包
        deb_name = [i['name'] for i in requests.get(deb_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.deb')]
        # 循环遍历下载kernel deb
        for deb in deb_name:
            if deb.endswith('.deb'):
                print(f'wget https://oss.mthreads.com/sw-build/{deb} -P ./daily/kernel/')
                pass  # 执行下载

    def get_iso(self):
        # 编码仓库地址
        prefix = self.enbase(f'Sw_Bsp_PreRelease/m1000-daily/master/aibook/')
        # 拼接requests url
        master_url = f'{self.url}{self.buckets}release-rc/objects?prefix={prefix}'
        # 获取 iso列表
        iso_name = [i['name'] for i in requests.get(master_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.iso')]
        # print(iso_name)
        # 下载iso
        print(f'wget https://oss.mthreads.com/release-rc/{iso_name[-1]} -P ./daily/iso/')

    def enbase(self, path):
        prefix = base64.b64encode(path.encode()).decode()
        return prefix

    def debase(self, path):
        prefix = base64.b64decode(path.encode()).decode()
        return prefix


if __name__ == '__main__':
    fp = Autoinstall()
    fp.get_session()
    # fp.get_gpu_driver()
    # fp.get_kernels()
    # fp.get_buckets()
    # fp.get_gr_umd()
    fp.get_iso()
