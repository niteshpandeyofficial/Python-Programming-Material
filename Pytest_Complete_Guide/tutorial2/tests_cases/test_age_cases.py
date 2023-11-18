import pytest
from tutorial2.myapp import validate_age

def test_validate_valid():
    validate_age(16)


def test_validate_invalid2():
    """
    When we check only for value which satisfied the condition then it raise the error but 
    it is valid condition so that our code should pass in this scenerio hence we use pytest.raises
    to valid the raise error and accordingly pass the cases
    """
    with pytest.raises(ValueError) as ex_info:
        validate_age(-5)
    assert str(ex_info.value)=='Age should not be less than 0'



def test_validate_invalid():
    with pytest.raises(ValueError,match='Age should not be less than 0'):
        validate_age(-5)