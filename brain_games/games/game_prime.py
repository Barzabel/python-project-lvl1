import random
from ..math_for_game.math import is_prime_number


def game_prime() -> None:
    """Answer "yes" if given number is prime. Otherwise answer "no"."""
    rand = random.randint(0, 200)
    question = f"Question: {rand}"
    is_prime = is_prime_number(rand)
    if is_prime:
        answer = "yes"
    else:
        answer = "no"

    return question, answer
