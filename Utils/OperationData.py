# 使用pandas操作Excel/csv文件
import os
import pandas
import re
from collections import ChainMap
import logging


class OperationData(object):
    def __init__(self, file_name):
        base_path = os.path.dirname(os.path.dirname(__file__))  # 上一级路径
        data_path = os.path.join(base_path, 'Data')  # Data路径
        file_path = os.path.join(data_path, file_name)  # Data中的文件路径

        # 判断文件后缀
        if file_name.endswith('.xls'):
            self.table = pandas.read_excel(file_path, keep_default_na=False)  # 读取Excel表格,只能读取xls格式结尾的
        elif file_name.endswith('.csv'):
            self.table = pandas.read_csv(file_path, keep_default_na=False)  # 读取csv文件
        else:
            self.table = None
            print('文件格式错误,只能读取csv或xls')

    def get_data_list(self):
        """
        读取数据格式为列表嵌套列表
        :return: [[],[],[]...]
        """
        if self.table is not None:
            return self.table.values.tolist()

    def get_data_dict(self):
        """
        读取数据格式为列表嵌套字典
        :return: [{},{},{}...]
        """
        if self.table is not None:
            return [self.table.loc[i].to_dict() for i in self.table.index.values]


if __name__ == '__main__':

    # op = OperationData('iozone.csv')
    # data = op.get_data_list()
    # print(op.get_data_dict())
    # a = [i[0] for i in data]
    # print(a)
    ioz_res = """
2025-02-24 16:31:22,111 - Utils.Base_init - INFO - 
exec cmd：iozone -r 512 -i 0 -i 1  -s 20G -I

2025-02-24 16:31:22,111 - Utils.Base_init - INFO - 
sucess ：Iozone: Performance Test of File I/O
	        Version $Revision: 3.489 $
		Compiled for 64 bit mode.
		Build: linux 

	Contributors:William Norcott, Don Capps, Isom Crawford, Kirby Collins
	             Al Slater, Scott Rhine, Mike Wisner, Ken Goss
	             Steve Landherr, Brad Smith, Mark Kelly, Dr. Alain CYR,
	             Randy Dunlap, Mark Montague, Dan Million, Gavin Brebner,
	             Jean-Marc Zucconi, Jeff Blomberg, Benny Halevy, Dave Boone,
	             Erik Habbinga, Kris Strecker, Walter Wong, Joshua Root,
	             Fabrice Bacchella, Zhenghua Xue, Qin Li, Darren Sawyer,
	             Vangel Bojaxhi, Ben England, Vikentsi Lapa,
	             Alexey Skidanov, Sudhir Kumar.

	Run began: Mon Feb 24 16:30:53 2025

	Record Size 512 kB
	File size set to 20971520 kB
	O_DIRECT feature enabled
	Command line used: iozone -r 512 -i 0 -i 1 -s 20G -I
	Output is in kBytes/sec
	Time Resolution = 0.000001 seconds.
	Processor cache size set to 1024 kBytes.
	Processor cache line size set to 32 bytes.
	File stride size set to 17 * record size.
                                                              random    random     bkwd    record    stride                                    
              kB  reclen    write  rewrite    read    reread    read     write     read   rewrite      read   fwrite frewrite    fread  freread
        20971520     512  3133137  3352519  3686231  3586579                                                                                  

iozone test complete.
 
    """
    # re_result = re.search('(\s+[0-9]{7}){4}', ioz_res)

    op = OperationData('iozone.csv')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dict_list = dict(ChainMap(*op.get_data_dict()))
    print(len(str(dict_list['reclen'])))
    re_result = re.search(r'(\s+[0-9]{7}){4}', ioz_res)
    print(re_result)
    re_list = [i for i in re_result.group(0).strip().split(' ') if i != '']
    print(re_list)
    list_history = dict_list['history_result'].split(' ')
    print(list_history)
    l = [i for i in re_list for j in list_history if int(i) / int(j) < 0.95]
    print(len(set(l)))
