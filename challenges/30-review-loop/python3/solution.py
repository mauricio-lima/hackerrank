#!/bin/python3

import sys


n = int(input())
for item in range(n):
    word = input()
    word = list(word)
    
    even = ''
    odd  = ''
    for position in range(len(word)):
        if position % 2:
            even += word[position]
        else:
            odd  += word[position]

    print(odd, even)    
