#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the profit function below.
def profit(b, s, c):
    # Return the fixed profit.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bsc = input().split()

        b = int(bsc[0])

        s = int(bsc[1])

        c = int(bsc[2])

        result = profit(b, s, c)

        fptr.write(str(result) + '\n')

    fptr.close()
