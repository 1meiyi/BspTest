import logging
import paramiko
import re
from Utils.OperationData import OperationData
from collections import ChainMap
from time import sleep


class BspTest:
    ssh = None

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ssh = paramiko.SSHClient()
        # self.log = logging
        self.log = logging.getLogger(__name__)
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
        sleep(30)
        if stdin:
            self.log.info(f'\nexec cmd：%s\n', cmd)
        if stdout:
            self.log.info('\nsucess ：%s\n', stdout.strip())
        else:
            self.log.warning('\nNone output\n')
        if stderr:
            self.log.error('\nerror：%s\n', stderr.strip())
        return stdout

    def close(self):
        self.ssh.close()

    def get_dict_result(self, res_path):
        op = OperationData(res_path)
        dict_list = dict(ChainMap(*op.get_data_dict()))
        return dict_list

    def assert_Iozone(self, ioz_res):
        global len_better
        op = OperationData('iozone.csv')
        dict_list = dict(ChainMap(*op.get_data_dict()))
        if len(str(dict_list['reclen'])) == 3:
            re_result = re.search(r'(\s+[0-9]{7}){4}', ioz_res)
            if re_result == None:
                logging.warning('测试数据未正常获取')
                return False
            else:
                re_list = [i for i in re_result.group(0).strip().split(' ') if i != '']
                print(re_list)
                list_history = dict_list['history_result'].split(' ')
                print(list_history)
                len_better = [i for i in re_list for j in list_history if int(i) / int(j) < 0.95]
                if len_better == 0:
                    logging.info(f'测试通过！测试数据：{list_history} 符合预期')
                else:
                    logging.warning(f'测试不通过：测试数据：{list_history} 低于历史数据 {re_list} ')
                    return False
            return len_better
            # if len(set(len_better)) == 4:
            #     logging.info(f'测试通过！测试数据：{list_history} 符合预期')
            # else:
            #     logging.warning(f'测试不通过：测试数据：{list_history} 低于历史数据 {dict_list['history_result']} ')
        elif len(str(dict_list['reclen'])) == 4:
            re_result = re.search(r'(\s+[0-9]{7}){4}', ioz_res)
            if re_result == None:
                logging.warning('测试数据未正常获取')
                return False
            else:
                re_list = [i for i in re_result.group(0).strip().split(' ') if i != '']
                # print(re_list)
                list_history = dict_list['history_result'].split(' ')
                # print(list_history)
                len_better = [i for i in re_list for j in list_history if int(i) / int(j) < 0.95]
                if len_better == 0:
                    logging.info(f'测试通过！测试数据：{list_history} 符合预期')
                else:
                    logging.warning(f'测试不通过：测试数据：{list_history} 低于历史数据 {re_list} ')
                    return False
            return len_better

