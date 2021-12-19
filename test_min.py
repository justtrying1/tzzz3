from random import randint, seed

import numpy

import main


def random_array(low, high, length):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def test_stress():
    seed(42)
    for i in range(10_000):
        array = sorted(random_array(-100, 100, 1000))
        assert numpy.min(array) == main.find_min(array)
