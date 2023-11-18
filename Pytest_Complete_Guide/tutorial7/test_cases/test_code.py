from unittest import mock
from tutorial7.code.sample_code import random_sum

@mock.patch("tutorial7.code.sample_code.random.randint")
def test_random_val(mock_randint):
    mock_randint.side_effect=[3,4]
    assert random_sum()==7


@mock.patch("tutorial7.code.sample_code.random.randint")
@mock.patch("tutorial7.code.sample_code.time.time")
@mock.patch("tutorial7.code.sample_code.requests.get")
def test_silly(mock_request_get,mock_time,mock_randint):
    test_params={"timestamp":123,"number":1234}
    
    mock_request_get=mock.Mock()
