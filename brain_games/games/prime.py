import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number) -> bool:
    if number % 2 == 0 or number < 2:
        return False
    for x in range(3, int(number ** 0.5) + 1, 2):
        if number % x == 0:
            return False
    return True


def generate_data_for_round() -> None:
    rand = random.randint(0, 200)
    question = f"{rand}"
    is_prime = is_prime_number(rand)
    if is_prime:
        answer = "yes"
    else:
        answer = "no"

    return question, answer
