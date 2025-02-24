import logging
import paramiko
import re
from Utils.OperationData import OperationData
from collections import ChainMap

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BspTest:
    ssh = None

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.log = logging.getLogger(self.__class__.__name__)
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def login(self, host):
        try:
            self.ssh.connect(host, port=22, username='swqa', password='gfx123456')
            self.log.info('Connected to %s successfully.', host)
        except Exception as e:
            self.log.error('Failed to connect to %s: %s', host, e)
            raise

    def send(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if stdin:
            print(self.log.info(f'\nexec cmd：%s', cmd))
        if stdout:
            print(self.log.info('\nsucess ：%s', stdout.strip()))
        else:
            print(self.log.warning('\nNone output'))
        if stderr:
            print(self.log.error('\nerror：%s', stderr.strip()))
        return stdout

    def close(self):
        self.ssh.close()

    def get_dict_result(self, res_path):
        op = OperationData(res_path)
        dict_list = dict(ChainMap(*op.get_data_dict()))
        return dict_list

    def assert_Iozone(self, ioz_res):
        dict_list = self.get_dict_result('a.csv')
        # return_res = re.findall('([0-9]{8})\s+([0-9]{4})\s+([0-9]{7})\s+([0-9]{7})\s+([0-9]{7})\s+([0-9]{7})', ioz_res)
        return_res = re.findall('([0-9]{8})\s+([0-9]{4}){\s+([0-9]{7})}{3}', ioz_res)
        for i in return_res:
            ast = '{:.2}'.format(int(i[2]) / int(dict_list['write']))
            ast1 = '{:.2}'.format(int(i[3]) / int(dict_list['rewrite']))
            ast2 = '{:.2}'.format(int(i[4]) / int(dict_list['read']))
            ast3 = '{:.2}'.format(int(i[5]) / int(dict_list['reread']))
            if float(ast) >= 0.95 and float(ast1) >= 0.95 and float(ast2) >= 0.95 and float(ast3) >= 0.95:
                print(self.log.info('断言成功', f'\n历史数据{dict_list['history_result']}' + f'\n测试数据：{return_res}'))
            else:
                print(self.log.warning('断言失败', f'\n历史数据{dict_list['history_result']}' + f'\n测试数据：{return_res}'))
