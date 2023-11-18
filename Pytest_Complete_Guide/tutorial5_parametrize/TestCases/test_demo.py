import pytest
from tutorial4_parametrize.SampleCode.main import add_number


def test_add_num():
    assert add_number(1,2)==3

def test_add_str():
    assert add_number(3,6)==9

def test_add_list():
    assert add_number([1,2],[3])==[1,2,3]

@pytest.mark.parametrize("a,b,c",[(1,2,3),('a','b','ab'),([1,2],[3],[1,2,3])],ids=["num","add","list"])
def test_add(a,b,c):
    """
    This complete code work as above 3 test cases.
    Parametrize marker help to write multiple test cases within single function.
    """
    assert add_number(a,b)==c




