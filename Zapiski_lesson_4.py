# from random import random, randint
# a = randint(1, 15)
# print(a)
# from sys import argv
# print(argv)
import math

б
def num_generator(end):
    num = 0
    while num <= end:
        yield num
        print("перезарядка")
        num += 1

numberator = num_generator(10)

print(next(numberator))
print(next(numberator))

# math.asin()