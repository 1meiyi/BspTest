# 使用pandas操作Excel/csv文件
import os
import pandas
import re
from collections import ChainMap

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

    op = OperationData('a.csv')
    data = op.get_data_list()
    print(op.get_data_dict())
    a = [i[0] for i in data]
    print(a)