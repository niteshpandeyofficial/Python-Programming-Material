from tutorial6_mock.code.sample import guess_number
from unittest import mock

# def test_roll_dice_num():
#     assert guess_number(3)=='you won' #there is less chance to get the same number which we will specified


@mock.patch("tutorial6_mock.code.sample.roll_dice")
def test_roll_dice_num(mock_roll_dice):
    mock_roll_dice.return_value=3  #always return the value provided instead of random number
    assert guess_number(3)=='you won'