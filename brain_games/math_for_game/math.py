import random


def get_nod(a, b) -> int:
    '''Наименьший общий елитель'''
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return get_nod(a % b, b)


def is_prime_number(x) -> bool:
    '''метод ферма'''
    if x in [ 2, 3, 5, 7]:
        return True
    elif x == 0 or x == 1:
        return False
    for _ in range(100):
        a = random.randint(2, x - 1)
        if get_nod(x, a) != 1:
            return False
        if pow(a, x - 1, x) != 1:
            return False
    return True
