import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number) -> bool:
    if (number != 2 and number % 2 == 0) or number < 2:
        return False
    for x in range(3, int(number ** 0.5) + 1, 2):
        if number % x == 0:
            return False
    return True


def generate_data_for_round() -> None:
    random_number = random.randint(0, 200)
    question = f"{random_number}"
    if is_prime(random_number):
        answer = "yes"
    else:
        answer = "no"

    return question, answer
