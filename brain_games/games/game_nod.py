import random


DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_nod(a, b) -> int:
    '''Наименьший общий елитель'''
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return get_nod(a % b, b)


def game_nod() -> None:
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    question = f"{rand1} {rand2}"
    ansver = get_nod(rand1, rand2)
    return question, str(ansver)
