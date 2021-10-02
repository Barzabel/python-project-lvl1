import random

from ..math_for_game.math import ferma


def game_prime():
    """Answer "yes" if given number is prime. Otherwise answer "no"."""
    rand = random.randint(0, 200)
    question = f"Question: {rand}"
    is_prime = ferma(rand)
    if is_prime:
    	answer = "yes"
    else:
    	answer = "no"

    return question, answer
