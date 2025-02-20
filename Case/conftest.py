import pytest
from Utils.Base_init import BspTest

@pytest.fixture()
def tear_down():
    fp = BspTest()
    fp.close()
