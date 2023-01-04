#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = 10
if number < 0:
    number = number * -1
    num = num % 10
    num = num * -1
else:
    num = number % 100
    print("Last digit of {} is ".format(num), end='')
    if num > 5:
        print("{} and is greater than 5".format(num))
    elif num == 0:
        print("{} and is 0".format(num))
    elif num < 6 and num != 0:
        print("is {} and is less than 6 and not 0".format(num))
