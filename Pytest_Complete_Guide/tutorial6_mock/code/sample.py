from tutorial6_mock.code.dice import roll_dice


def guess_number(num):
    result=roll_dice()
    if result==num:
        return "you won"
    else:
        return "you lost"