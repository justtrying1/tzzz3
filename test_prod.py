import math
from random import randint, seed

import numpy

import main


def random_array(low, high, length):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def prod(array):
    a = 1
    for i in array:
        a *= i
    return a


def test_stress():
    seed(42)
    for i in range(10_000):
        array = sorted(random_array(-100, 100, 1000))
        assert math.prod(array) == main.find_prod(array)
