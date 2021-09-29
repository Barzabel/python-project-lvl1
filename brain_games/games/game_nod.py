import random


def get_nod(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return get_nod(a % b, b)


def game_nod():
    """Find the greatest common divisor of given numbers."""
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    question = f"Question: {rand1} {rand2}"
    ansver = get_nod(rand1, rand2)
    return question, str(ansver)
