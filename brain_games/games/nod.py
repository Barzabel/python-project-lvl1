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


def generate_data_for_round() -> None:
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f"{random_number1} {random_number2}"
    ansver = get_nod(random_number1, random_number2)
    return question, str(ansver)
