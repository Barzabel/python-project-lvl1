import random


DESCRIPTION = "What is the result of the expression?"


def generate_data_for_round():
    operator = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
    }
    random_number1 = random.randint(0, 100)
    random_number2 = random.randint(0, 100)
    random_operator = random.choice(["+", "*", "-"])
    question = f"{random_number1} {random_operator} {random_number2}"
    right_answer = operator[random_operator](random_number1, random_number2)
    return question, str(right_answer)
