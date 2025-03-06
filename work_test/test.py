# import requests
# import json
# from requests.auth import HTTPBasicAuth
# from requests.utils import dict_from_cookiejar

# payload = json.dumps({
#     "accessKey": "mtoss",
#     "secretKey": "mtoss123"
# })
# headers = {
#     'Content-Type': 'application/json'
# }
# url = 'https://oss.mthreads.com:9001/api/v1/login'
# session = requests.session()
# # data = bytes(payload, encoding='utf8')
# response = session.post(url, data=payload, headers=headers)
#
# # print(session.cookies.get_dict(), '###############################################')
# cookies_dict = dict_from_cookiejar(response.cookies)
# print(cookies_dict, '**********************************')
# print(response.status_code)
# for i in range(5):
#     if response.status_code == 201:
#         print(response.status_code)
#         print(response.headers)
#         print(response.cookies)
#         break
#     else:
#         print(f'第{i + 1}次尝试连接')
#         continue
# rs = session.get(
#     'https://oss.mthreads.com:9001/api/v1/buckets/product-release/objects?prefix=cmVsZWFzZV9NMTAwMF8xLjIuMC8yMDI1MDIyNi8=')
#     # 'https://oss.mthreads.com:9001/api/v1/buckets/product-release/objects?prefix=cmVsZWFzZV9NMTAwMF8xLjIuMC8yMDI1MDMwMw='
# print(rs.json())
# import datetime
#
# print(datetime.date.today().strftime('%Y%m%d'))
import re

tst = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>代码提交信息</title>

    <meta name="description" content="Source code generated using layoutit.com">
    <meta name="author" content="LayoutIt!">

    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">

  </head>
  <body>

    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <table class="table">
            <thead>
              <tr>
                  <th>Short ID</th>
                  <th>Commit ID</th>
                  <th>Commit Time</th>
                  <th>Commit msg</th>
                  <th>Author</th>
              </tr>
            </thead>
            <tbody>

              <tr>
                <td name="short_id">101e2d503</td>
                <td name="commit_id">101e2d5037f19f45076472b1e681f8eb8da932d2</td>
                <td name="commit_time">2025-02-28 17:39:03</td>
                <td name="commit_msg">Merge mtgpu-next: add vm_ctx ref count</td>
                <td name="author">shen.yang</td>
              </tr>
              
              <tr>
                <td name="short_id">f899a4a31</td>
                <td name="commit_id">f899a4a318f56b973b9e4c630576143f8921f896</td>
                <td name="commit_time">2025-02-28 15:27:02</td>
                <td name="commit_msg">Merge mtgpu-next: fix fwif fw_va for riscv fw</td>
                <td name="author">lijun.fang</td>
              </tr>
              
              <tr>
                <td name="short_id">d643708cd</td>
                <td name="commit_id">d643708cd63f53a7ae645f1b715e494cbb559914</td>
                <td name="commit_time">2025-02-28 14:59:00</td>
                <td name="commit_msg">mtgpu: vgpu: remove unnecessary prints</td>
                <td name="author">enbei.liu</td>
              </tr>
              
              <tr>
                <td name="short_id">ead6ea201</td>
                <td name="commit_id">ead6ea20119fe7d8c86203a4603a28bf78672693</td>
                <td name="commit_time">2025-02-28 11:17:39</td>
                <td name="commit_msg">pvr: avoid sleeping in CPU interrupt atomic context</td>
                <td name="author">owen.zhang</td>
              </tr>
              
              <tr>
                <td name="short_id">2399117d2</td>
                <td name="commit_id">2399117d2129243b4b34577cd2ec3eae3a7bdfb4</td>
                <td name="commit_time">2025-02-28 11:04:17</td>
                <td name="commit_msg">mtgpu-next: submit cancel and terminate cmd when process exit</td>
                <td name="author">min.du</td>
              </tr>
              
              <tr>
                <td name="short_id">371905a79</td>
                <td name="commit_id">371905a79b448f4729c13530feba0a500a2998e8</td>
                <td name="commit_time">2025-02-28 10:57:59</td>
                <td name="commit_msg">Merge mtgpu: dma semaphore modify</td>
                <td name="author">bowang.geng</td>
              </tr>
              
              <tr>
                <td name="short_id">1f082d872</td>
                <td name="commit_id">1f082d8721c2b8fdb64073f27230c522c0c50ecf</td>
                <td name="commit_time">2025-02-28 10:05:25</td>
                <td name="commit_msg">Merge mtgpu: get fw commit id</td>
                <td name="author">bowang.geng</td>
              </tr>
              
              <tr>
                <td name="short_id">43e959a3e</td>
                <td name="commit_id">43e959a3e9c5601c189bf460d94a1b34f9b22858</td>
                <td name="commit_time">2025-02-28 10:00:21</td>
                <td name="commit_msg">mtgpu: bugfix GPUReset bitmask.</td>
                <td name="author">changhao.xin</td>
              </tr>
              
              <tr>
                <td name="short_id">6d2014d50</td>
                <td name="commit_id">6d2014d5031da15b5b112798193601b4083c33a4</td>
                <td name="commit_time">2025-02-28 08:39:49</td>
                <td name="commit_msg">mtgpu-next: fix fwif fw_va for riscv fw</td>
                <td name="author">lijun.fang</td>
              </tr>
              
              <tr>
                <td name="short_id">48c03cc2f</td>
                <td name="commit_id">48c03cc2fd41355dd5c4e135931b99d731c8a5f6</td>
                <td name="commit_time">2025-02-27 19:55:26</td>
                <td name="commit_msg">mtgpu-next: add job_ctx ref count</td>
                <td name="author">shen.yang</td>
              </tr>
              
              <tr>
                <td name="short_id">b946c57ae</td>
                <td name="commit_id">b946c57ae7a5c125dbcede2e5d0edf3aad7f8d98</td>
                <td name="commit_time">2025-02-27 19:51:22</td>
                <td name="commit_msg">vpu: try to fix vVPU compatible issue.</td>
                <td name="author">yonggang.zhao</td>
              </tr>
              
              <tr>
                <td name="short_id">7c5d5411c</td>
                <td name="commit_id">7c5d5411cf7b0b2695825b7c84d9327b31dcb594</td>
                <td name="commit_time">2025-02-27 17:25:59</td>
                <td name="commit_msg">mtgpu: vgpu: fix build error on linux-guest</td>
                <td name="author">zijian.zhang</td>
              </tr>
              
              <tr>
                <td name="short_id">33af0809c</td>
                <td name="commit_id">33af0809cf2fd2429460e3288d529b7feaccc33e</td>
                <td name="commit_time">2025-02-27 16:21:01</td>
                <td name="commit_msg">Merge mtgpu: increase the driver&#39;s minor version to 1</td>
                <td name="author">xiaolong.he</td>
              </tr>
              
              <tr>
                <td name="short_id">b5c2514c3</td>
                <td name="commit_id">b5c2514c30334647d0651778e9bb7d8602949f66</td>
                <td name="commit_time">2025-02-27 15:27:15</td>
                <td name="commit_msg">Merge vgpu: init mpc_conf in mtgpu_probe</td>
                <td name="author">jie.li</td>
              </tr>
              
              <tr>
                <td name="short_id">366629be6</td>
                <td name="commit_id">366629be657af90f33f14f9e6898d8ce3c1f8b2c</td>
                <td name="commit_time">2025-02-27 14:00:32</td>
                <td name="commit_msg">mtgpu: increase the driver&#39;s minor version to 1</td>
                <td name="author">owen.zhang</td>
              </tr>
              
              <tr>
                <td name="short_id">fd403a459</td>
                <td name="commit_id">fd403a459dc2297732746e31dbbbba867cb5e7b8</td>
                <td name="commit_time">2025-02-27 11:37:07</td>
                <td name="commit_msg">Merge mtgpu: synchronize code to the develop branch</td>
                <td name="author">bowang.geng</td>
              </tr>
              
              <tr>
                <td name="short_id">df2033356</td>
                <td name="commit_id">df20333564bb82b0feff070cbcc83122e95d4145</td>
                <td name="commit_time">2025-02-27 11:06:01</td>
                <td name="commit_msg">mtgpu: dma semaphore modify</td>
                <td name="author">bowang.geng</td>
              </tr>
              
              <tr>
                <td name="short_id">e4abf3cbd</td>
                <td name="commit_id">e4abf3cbdc6c56b15c262117d76c479bf7800cc5</td>
                <td name="commit_time">2025-02-27 10:45:23</td>
                <td name="commit_msg">vgpu: init mpc_conf in mtgpu_probe</td>
                <td name="author">jie.li</td>
              </tr>
              
              <tr>
                <td name="short_id">0a443afc1</td>
                <td name="commit_id">0a443afc1a10a91684c8a79b6426044b1d864abf</td>
                <td name="commit_time">2025-02-27 10:02:21</td>
                <td name="commit_msg">Merge mtgpu: vgpu: optimize VF driver loading process</td>
                <td name="author">zijian.zhang</td>
              </tr>
                            
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/scripts.js"></script>
  </body>
</html>
"""
from bs4 import BeautifulSoup

# dict_data = {}
# list_commit = []
# dict_data['short_id'] = [i.get_text() for i in soup.find_all('td', attrs={'name': 'short_id'})]
# dict_data['commit_id'] = [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_id'})]
# dict_data['commit_time'] = [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_time'})]
# dict_data['commit_msg'] = [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_msg'})]
# dict_data['author'] = [i.get_text() for i in soup.find_all('td', attrs={'name': 'author'})]
# for short_id, commit_id, commit_time, commit_msg, author in zip(dict_data['short_id'], dict_data['commit_id'],
#                                                                 dict_data['commit_time'], dict_data['commit_msg'],
#                                                                 dict_data['author']):
#     commit = {
#         'short_id': short_id,
#         'commit_id': commit_id,
#         'commit_time': commit_time,
#         'commit_msg': commit_msg,
#         'author': author
#     }
#
#     list_commit.append(commit)
#     print(list_commit)

# soup = BeautifulSoup(tst, 'html.parser')
# list_commit = []
# dict_data = {'short_id': [i.get_text() for i in soup.find_all('td', attrs={'name': 'short_id'})],
#              'commit_id': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_id'})],
#              'commit_time': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_time'})],
#              'commit_msg': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_msg'})],
#              'author': [i.get_text() for i in soup.find_all('td', attrs={'name': 'author'})]}
# for short_id, commit_id, commit_time, commit_msg, author in zip(dict_data['short_id'], dict_data['commit_id'],
#                                                                 dict_data['commit_time'], dict_data['commit_msg'],
#                                                                 dict_data['author']):
#     commit = {
#         'short_id': short_id,
#         'commit_id': commit_id,
#         'commit_time': commit_time,
#         'commit_msg': commit_msg,
#         'author': author
#     }
#     list_commit.append(commit)
# for Merge in list_commit:
#     if 'Merge' in Merge['commit_msg']:
#         print(Merge)
        # print(list_commit)
#     del commit
# else:

# while True:
#     info = input('请选择并粘贴上面输出的commit_id：')
#     if re.search('[0-9a-z]{9}', info):
#         print(info)
#         break
#     else:
#         print('请重新输入！')
#         continue

"""
dkms remove mtgpu -v 1.0.0 --all
rm -rf /usr/src/mtgpu-1.0.0
dpkg -X 94c7840a7/94c7840a7_arm64-mtgpu_linux-xorg-release-hw.deb /
dkms add mtgpu -v 1.0.0 
dkms install mtgpu -v 1.0.0
"""
