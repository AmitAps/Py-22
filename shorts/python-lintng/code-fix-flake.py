import random


def myfunc():
    return random.randint(0, 100)


def multiply(a, b):
    return a * b


print(multiply(myfunc(), myfunc()))
