import random


def get_random_list():
    ls = []
    c = 1
    while c <= 10:
        ls.append(random.randint(1, 26))
        c +=1
    return ls

