import random


DESCRIPTION = "What number is missing in the progression?"


def game_progression() -> None:
    size = random.randint(6, 11)
    step = random.randint(2, 13)
    start = random.randint(1, 100)
    progression = [start + (x * step) for x in range(0, size)]
    index = random.randint(0, size - 1)
    answer = progression[index]
    progression[index] = ".."
    qustion = " ".join(map(str, progression))
    return qustion, str(answer)
