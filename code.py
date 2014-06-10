#!/bin/env python
import random


def my_func():
    return random.randint(0, 10)


for count in range(0, 10):
    print my_func()
