import pytest
import re
from Utils.Base_init import BspTest
from Utils.OperationData import OperationData

fp = BspTest()
data = OperationData('iozone.csv').get_data_list()


class TestIOzone:
    fp.login('192.168.117.149')

    @pytest.mark.parametrize('cmd', [i[0] for i in data])
    def test_01(self, cmd):
        ioz_res = fp.send(cmd)
        len_rs = fp.assert_Iozone(ioz_res)
        assert len_rs, 0


if __name__ == "__main__":
    pytest.main()
