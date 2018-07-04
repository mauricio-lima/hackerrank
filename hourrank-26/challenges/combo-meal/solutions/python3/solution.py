#!/bin/python3


import os


def profit(b, s, c):
	return b + s - c

	
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
