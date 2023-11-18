from tutorial1.SampleCode.main import add_number

def test_add():
    assert add_number(1,2)==3

def test_add_str():
    assert add_number(3,6)==9


class Test_all:
    """
    for class name first character should be capital  of Test (Test_all)
    for method name should be start with prefix test eg(test_add)
    """
    def test_new1(self):
        """
        concatenate the string value instead of addition
        """
        assert add_number('a','b')=='ab'


