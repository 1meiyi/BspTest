import pytest
import re
from Utils.Base_init import BspTest
from Utils.OperationData import OperationData

fp = BspTest()
data_iozone = OperationData('iozone.csv').get_data_list()
data_fio = OperationData('fio.csv').get_data_list()
data_dd = OperationData('dd.csv').get_data_list()


class TestIOzone:
    fp.login('192.168.117.87')

    @pytest.mark.description("IOzone性能测试: "
                             "http://qa-zentao.mthreads.com:9000/testcase-view-8387-9.html?tid=90w8fi48")
    @pytest.mark.parametrize('cmd', [i[0] for i in data_iozone])
    def test_01_iozone(self, cmd):
        ioz_res = fp.send(cmd)
        len_rs = fp.assert_Iozone(ioz_res)
        print(len_rs)
        assert len_rs, True

    @pytest.mark.description("fio硬盘性能测试: "
                             "http://qa-zentao.mthreads.com:9000/testcase-view-8388-7.html?tid=xen4k1po")
    @pytest.mark.parametrize('cmd', [i[0] for i in data_fio])
    def test_02_fio(self, cmd):
        fio_rs = fp.send(cmd)
        final_rs = fp.assert_fio(fio_rs)
        assert final_rs, True

    # @pytest.mark.description("fio硬盘性能测试: "
    #                          "http://qa-zentao.mthreads.com:9000/testcase-view-8388-7.html?tid=xen4k1po")
    # @pytest.mark.parametrize('cmd', [i[0] for i in data_dd])
    # def test_03_dd(self, cmd):
    #     dd_rs = fp.send(cmd)
    #     # final_rs = fp.ass


if __name__ == "__main__":
    pytest.main()
