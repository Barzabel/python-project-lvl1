import random


DESCRIPTION = "What is the result of the expression?"


def game_calc() -> None:
    operat = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
    }
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    operator = random.choice(["+", "*", "-"])
    question = f"Question: {rand1} {operator} {rand2}"
    ansver = operat[operator](rand1, rand2)
    return question, str(ansver)
