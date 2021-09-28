import random


def check_even():
    """Answer "yes" if the number is even, otherwise answer "no"."""
    rand = random.randint(0, 100)
    qustion = f'Question: {rand}'
    if rand % 2 == 0:
    	answer = "yes"
    else:
    	answer = "no"
    return qustion, answer
