import random

from ..math_for_game.math import get_nod


def game_nod() -> None:
    """Find the greatest common divisor of given numbers."""
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    question = f"Question: {rand1} {rand2}"
    ansver = get_nod(rand1, rand2)
    return question, str(ansver)
