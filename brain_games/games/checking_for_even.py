import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data_for_round() -> None:
    rand = random.randint(0, 100)
    question = f'{rand}'
    if rand % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return question, answer
