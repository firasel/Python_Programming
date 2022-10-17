import math
from time import time


def timer(func):
    def inner(*args, **kwargs):
        print('Time Start')
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'Time End. Total time taken {end - start}')
    return inner


@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')


# timer(get_factorial)()
get_factorial(n=20)
