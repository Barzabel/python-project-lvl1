import random


DESCRIPTION = "What is the result of the expression?"


def generate_data_for_round():
    operat = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
    }
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    operator = random.choice(["+", "*", "-"])
    question = f"{number1} {operator} {number2}"
    right_answer = operat[operator](number1, number2)
    return question, str(right_answer)
