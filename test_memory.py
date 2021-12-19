import tracemalloc
from random import seed, randint

import numpy

import main

tracemalloc.start()


def random_array(low, high, length):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def test_stress():
    seed(42)
    for i in range(10_000):
        array = sorted(random_array(-100, 100, 1000))
        assert numpy.sum(array) == main.find_sum(array)


print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
assert tracemalloc.get_traced_memory() < 500
