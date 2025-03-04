import logging
import paramiko
import re
from Utils.OperationData import OperationData
from collections import ChainMap
from time import sleep


class BspTest:
    ssh = None

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
            self.log.info(f'exec cmd：%s\n', cmd)
        if stdout:
            self.log.info('sucess ：%s\n', stdout.strip())
        else:
            self.log.warning('None output\n')
        if stderr:
            self.log.error('error：%s\n', stderr.strip())
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
            if re_result is None:
                logging.warning('测试数据不正常或参数错误')
                return False
            else:
                re_list = [i for i in re_result.group(0).strip().split(' ') if i != '']  # 测试数据
                list_history = dict_list['history_result'].split(' ')  # 历史数据
                len_better = len(set([i for i in re_list for j in list_history if int(i) / int(j) > 0.98]))
                # 测试数据除以历史数据大于0.98,增加新列表并去重
                if len_better == 4:
                    # 测试数据都大于x86对照组，返回四个数值。
                    logging.info(f'测试通过！测试数据：{re_list} 符合预期')
                    return True
                else:
                    gap_result = (int(re_list[0]) - int(list_history[0])) / int(list_history[0])
                    logging.warning(f'测试数据波动{float(gap_result):.2f}%,测试数据：{re_list} 低于低于X86对照组数据 {list_history} ')
                    return False
        elif len(str(dict_list['reclen'])) == 4:
            re_result = re.search(r'(\s+[0-9]{7}){4}', ioz_res)
            if re_result is None:
                logging.warning('测试数据未正常获取')
                return False
            else:
                re_list = [i for i in re_result.group(0).strip().split(' ') if i != '']
                # print(re_list)
                list_history = dict_list['history_result'].split(' ')
                # print(list_history)
                len_better = len(set([i for i in re_list for j in list_history if int(i) / int(j) > 0.98]))
                # 测试数据除以历史数据大于0.98,增加新列表并去重
                if len_better == 4:
                    # 测试数据都大于x86对照组，返回四个数值。
                    logging.info(f'测试通过！测试数据：{re_list} 符合预期')
                    return True
                else:
                    gap_result = (int(re_list[0]) - int(list_history[0])) / int(list_history[0])
                    logging.warning(f'测试数据波动{gap_result:.2f}%,测试数据：{re_list} 低于X86对照组数据 {list_history} ')
                    return False

    def assert_fio(self, fio_rs):
        op = OperationData('fio.csv')
        dict_list = dict(ChainMap(*op.get_data_dict()))
        IOPS = re.search(r'IOPS=((\d+.\w))', fio_rs).group(1).strip()
        run_time = re.search(r'(\d{5})-(\d{5}msec)', fio_rs).group(1).strip()
        # print(dict_list['IOPS'], type(dict_list['IOPS']))
        # print(dict_list['runtime'], type(dict_list['runtime']))
        if (float(IOPS) - float(dict_list['IOPS'])) / float(dict_list['IOPS']) < 0.98:
            logging.info((float(IOPS) - float(dict_list['IOPS'])) / float(dict_list['IOPS']) < 0.98)
            logging.info(IOPS,dict_list['IOPS'],dict_list['IOPS'])
            logging.info(f'x86对照数据：IOPS={dict_list['IOPS']}runtime={dict_list['runtime']}msec'
                            f' 测试数据：IOPS={IOPS} runtime={run_time}msec 无下降')
            return True
        else:
            logging.warning(f'测试数据波动{(float(IOPS) - float(dict_list['IOPS'])) / float(dict_list['IOPS']):.2f}%,'
                            f'测试数据：IOPS={IOPS} runtime={run_time}msec，'
                            f'x86对照数据：IOPS={dict_list['IOPS']}runtime={dict_list['runtime']}msec')
            return False
