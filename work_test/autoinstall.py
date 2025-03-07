import datetime
import re

import requests
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

    def get_gpu_driver(self, date):
        # timedate = datetime.date.today().strftime('%Y%m%d')
        # 编码仓库地址
        prefix = self.enbase('release_M1000_1.2.0/')
        # 拼接 url
        url = f'{self.url}{self.buckets}product-release/objects?prefix={prefix}'
        # 根据时间获取最新仓库

        time_date = [i['name'] for i in self.requests.get(url, headers=self.get_headers()).json()['objects']]
        roll_back_time = re.search('[0-9]{8}', time_date[-date]).group(0)
        deb_url = f'{self.url}{self.buckets}product-release/objects?prefix={self.enbase(f'release_M1000_1.2.0/{roll_back_time}/')}'
        # 筛选deb
        deb_name = [i['name'] for i in self.requests.get(deb_url.strip(), headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('glvnd-pc_arm64.deb')]
        self.send(f'wget https://oss.mthreads.com/product-release/{deb_name[0]} -P /home/swqa/daily/gpu/')
        print(f'正在下载：https://oss.mthreads.com/product-release/{deb_name[0]}')
        self.send('sudo dpkg -i /home/swqa/daily/gpu/*.deb')
        print('Gpu驱动 安装成功')
        self.send('sudo reboot')

    def get_kernels(self, date):
        timedate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # 编码kernel prefix
        prefix = self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/')
        # 拼接仓库日期Url
        master_url = f'{self.url}{self.buckets}sw-build/objects?prefix={prefix}'
        # 获取仓库日期
        time_date = [i['name'] for i in self.requests.get(master_url, headers=self.get_headers()).json()['objects']]
        # 拼接deb包 Url 20250222
        roll_back_time = re.search('[0-9]{8}', time_date[-date]).group(0)
        deb_url = f'{self.url}{self.buckets}sw-build/objects?prefix={self.enbase(f'{roll_back_time}kernel-debs/')}'
        # 筛选deb包
        deb_name = [i['name'] for i in requests.get(deb_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.deb')]
        # 循环遍历下载kernel deb
        deb_package = [i for i in deb_name if
                       i.endswith('.deb') and 'dbg' not in i and not i.startswith('linux-headers')]
        for i in deb_package:
            print(f'正在下载{i}')
            self.send(f'wget https://oss.mthreads.com/sw-build/{i} -P /home/swqa/daily/{roll_back_time}/kernel/')
        self.send(f'rm -rf /home/swqa/daily/{roll_back_time}/kernel/linux-headers*')
        cmd = f'sudo dpkg -i /home/swqa/daily/{roll_back_time}/kernel/*.deb'
        print(f'正在安装 exec_cmd:{cmd}')
        self.send(cmd)
        print('已完成安装')
        self.send('sudo reboot')

    def get_firmware(self, date):
        # 编码kernel prefix
        prefix = self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/')
        # 拼接仓库日期Url
        master_url = f'{self.url}{self.buckets}sw-build/objects?prefix={prefix}'
        # 获取仓库日期
        time_date = [i['name'] for i in self.requests.get(master_url, headers=self.get_headers()).json()['objects']]
        # 拼接deb包 Url 20250222
        roll_back_time = re.search('[0-9]{8}', time_date[-date]).group(0)
        wic_url = (f'{self.url}{self.buckets}sw-build/objects?prefix='
                   f'{self.enbase(f'm1000/daily/master/aibook-6.6-ubuntu/{roll_back_time}/firmware/')}')
        # 筛选deb包
        wic_name = [i['name'] for i in requests.get(wic_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.wic')]
        timedate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        for i in wic_name:
            print(f'正在下载{i}')
            self.send(f'wget https://oss.mthreads.com/sw-build/{i} -P /home/swqa/daily/{roll_back_time}/uefi/')
            self.send(f'rm -rf /home/swqa/daily/{roll_back_time}/uefi/m1000-image-aibook-evb.wic')
        cmd = f'sudo ac_tool firmware flash -w 0 -f  /home/swqa/daily/{roll_back_time}/uefi/*.wic'
        print(f'正在安装 exec_cmd:{cmd}')
        self.send(cmd)
        print('已完成安装固件')
        self.send('sudo reboot')

    def get_iso(self):
        # 编码仓库地址
        prefix = self.enbase(f'Sw_Bsp_PreRelease/m1000-daily/master/aibook/')
        # 拼接requests url
        master_url = f'{self.url}{self.buckets}release-rc/objects?prefix={prefix}'
        # 获取 iso列表
        iso_name = [i['name'] for i in requests.get(master_url, headers=self.get_headers()).json()['objects'] if
                    i['name'].endswith('.iso')]
        # 下载iso
        print(f'wget https://oss.mthreads.com/release-rc/{iso_name[-1]} -P ./daily/iso/')

    def enbase(self, path):
        prefix = base64.urlsafe_b64encode(path.encode()).decode()
        return prefix

    def debase(self, path):
        prefix = base64.urlsafe_b64decode(path.encode()).decode()
        return prefix

    def send(self, cmd):
        ex_cmd = Base_init.BspTest()
        ex_cmd.login('192.168.117.245')
        ex_cmd.send(cmd)
        ex_cmd.close()


if __name__ == '__main__':
    fp = Autoinstall()
    fp.get_session()
    fp.get_gpu_driver(15)
    # fp.get_kernels()
    # fp.get_firmware(20)
    # fp.get_buckets()
    # fp.get_gr_umd()
    # fp.get_iso()
