import datetime, main
import time

import numpy

for i in range(10):

    f = open(f"test_{i}", 'a+')  # open file in append mode
    for a in range((i+1)*100):
        f.write("999 "*(i+1))
    f.close()
result = []
length = []
for b in range(10):
    with open(f'test_{b}', 'r') as file:
        data = file.read().replace('\n', '')
        numbers = data.split(" ")
        numbers.remove("")
        numbers = [int(token) for token in numbers]

        t0 = datetime.datetime.now()
        main.find_min(numbers)
        main.find_sum(numbers)
        main.find_prod(numbers)
        main.find_max(numbers)
        t1 = datetime.datetime.now()
        t2 = datetime.datetime.now()
        numpy.min(numbers)
        numpy.sum(numbers)
        numpy.prod(numbers)
        numpy.max(numbers)
        t3 = datetime.datetime.now()
        result.append(t1-t0)
        length.append((t3-t2))
for a in range(len(result)):
    print(result[a])
    print(length[a])
    try:

        assert result[a] <= length[a]
    except IndexError:
        pass