import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data_for_round() -> None:
    random_number = random.randint(0, 100)
    question = f'{random_number}'
    if random_number % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer
