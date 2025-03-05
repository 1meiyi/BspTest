import requests
import re
from bs4 import BeautifulSoup
import Base_init

pc = Base_init.BspTest()


def get_commit_rs():
    while True:
        rep = input('\n1、kmd\n2、umd \n请选择回退选项: ')
        if rep not in ['1', '2']:
            print('输入错误，请重新输入回退选项：')
            continue
        branch_num = input('\n1、develop \n2、release_M1000_1.2.0 \n3、release_2.5.0 \n请选择branch: ')
        if branch_num not in ['1', '2', '3']:
            print('输入错误，请重新输入branch：')
            continue
        begin_timer = input('\n请选择开始查找时间 例如 2025-03-03：')
        end_timer = input('\n请选择查找结束时间 例如 2025-03-04：')
        if not (re.match(r'\d{4}-\d{2}-\d{2}', begin_timer) and re.match(r'\d{4}-\d{2}-\d{2}', end_timer)):
            print('输入时间格式异常！例如：2025-03-03')
            continue
        if rep == '1':
            repo = 'gr-kmd'
        elif rep == '2':
            repo = 'gr-umd'
        if branch_num == '1':
            branch = 'develop'
        elif branch_num == '2':
            branch = 'release_M1000_1.2.0'
        elif branch_num == '3':
            branch = 'release_2.5.0'
        url = f'http://192.168.114.118/td/code_commit/list?repo={repo}&branch={branch}&begin_time={begin_timer}+00%3A00%3A00&end_time={end_timer}+00%3A00%3A00'
        res = requests.get(url)
        rs = res.text
        return rs


def get_commit_info():
    soup = BeautifulSoup(get_commit_rs(), 'html.parser')
    list_commit = []
    dict_data = {'short_id': [i.get_text() for i in soup.find_all('td', attrs={'name': 'short_id'})],
                 'commit_id': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_id'})],
                 'commit_time': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_time'})],
                 'commit_msg': [i.get_text() for i in soup.find_all('td', attrs={'name': 'commit_msg'})],
                 'author': [i.get_text() for i in soup.find_all('td', attrs={'name': 'author'})]}
    for short_id, commit_id, commit_time, commit_msg, author in zip(dict_data['short_id'], dict_data['commit_id'],
                                                                    dict_data['commit_time'], dict_data['commit_msg'],
                                                                    dict_data['author']):
        commit = {
            'short_id': short_id,
            'commit_id': commit_id,
            'commit_time': commit_time,
            'commit_msg': commit_msg,
            'author': author
        }
        list_commit.append(commit)
    return list_commit


def ger_frame_text():
    pc.login('192.168.117.198')
    res = pc.send("lscpu | awk -F' ' '{print $2}' | head -n 1")
    if res is None:
        print('架构数据未捕获')
    else:
        return res


def choose_download():
    for Merge in get_commit_info():
        if 'Merge' in Merge['commit_msg']:
            print(Merge)
    while True:
        info = input('请选择并粘贴上面输出的commit_id：')
        # if info == Merge['short_id']:
        #     print(Merge, '符合id')
        if re.search('[0-9a-z]{9}', info):
            print(info, '符合')
            return info
        else:
            print('请重新输入！')
            continue

if __name__ == '__main__':

    choose_download()
