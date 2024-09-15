import time


def measure_time(func):
    start = time.time()
    func()
    end = time.time()
    return end-start

def powers(limit):
    return [x**2 for x in range(limit)]



print(measure_time(lambda:powers(3264635)))


import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))

print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))