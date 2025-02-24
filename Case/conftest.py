import pytest
from Utils.Base_init import BspTest

fp = BspTest()





@pytest.fixture()
def tear_down():
    fp = BspTest()
    fp.close()
