#!/bin/python3

import sys

def getPoints(month1, month2, month3):
    return sum([100 if cards > 10 else cards * 10 for cards in [month1, month2, month3]])
        

month1,month2,month3 = input().strip().split(' ')
month1,month2,month3 = [int(month1),int(month2),int(month3)]
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)
