import pytest
import re
from Utils.Base_init import BspTest
from Utils.OperationData import OperationData


fp = BspTest()
data = OperationData('a.csv').get_data_list()

class TestIOzone:
    fp.login('192.168.117.29')

    @pytest.mark.parametrize('cmd', [i[0] for i in data])
    def test_01(self, cmd):
        ioz_res = fp.send(cmd)
        fp.assert_Iozone(ioz_res)






if __name__ == "__main__":
    pytest.main()
