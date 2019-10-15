#!/bin/python3

import sys


n = int(input().strip())
array = [int(item) for item in input().strip().split(' ')]

for position in range(len(array)):
    print(array[len(array) - position - 1], end=' ')