#!/bin/python3

import sys


s = input().strip()
try:
    print(int(s))
except ValueError:
    print('Bad String')
    
