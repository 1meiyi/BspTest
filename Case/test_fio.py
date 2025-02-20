import pytest
from Utils.Base_init import BspTest

fp = BspTest()
class TestIOzone:


    def test_01(self):
        rs = fp.send('ls -l')
        print(rs)

    def test_02(self):
        """
        """
        rs = fp.send('ls -l')
        print(rs)


if __name__ == "__main__":
    pytest.main()
