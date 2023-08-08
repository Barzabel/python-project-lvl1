import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_check_even() -> None:
    rand = random.randint(0, 100)
    qustion = f'{rand}'
    if rand % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return qustion, answer
