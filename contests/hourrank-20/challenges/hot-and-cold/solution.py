#!/bin/python3

import sys

def isSatisfiable(c1, c2, h1, h2):
    if h1 >= c1 and h1 >= c2 and h2 >= c1 and h2 >= c2:
        return 'YES'
    
    return 'NO'
    
    

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)

