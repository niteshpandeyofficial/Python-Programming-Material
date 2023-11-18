import pytest
from datetime import datetime
from tutorial4_fixture.SampleCode.Student import Student


@pytest.fixture
def dummy_student():
    return Student("Nitesh",datetime(2000,1,1),"Admin")


def test_student_get_age(dummy_student):
    age_data=(datetime.now()-dummy_student.dob).days // 365
    assert dummy_student.get_age()==age_data

def test_age(dummy_student):
    dummy_student.set_credits(10)


