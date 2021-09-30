import random


def progression_game():
    """What number is missing in the progression?"""
    size = random.randint(6, 11)
    step = random.randint(2, 13)
    start = random.randint(1,100)
    progression = [start + (x * step) for x in range(0, size)]
    index = random.randint(0, size - 1)
    answer = progression[index]
    progression[index] = ".."
    qustion = " ".join(map(str, progression))
    return qustion, str(answer)
