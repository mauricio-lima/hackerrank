


#!/bin/python3

import sys
import itertools


def root(i):
    while not i == unions[i]:
        unions[i] = unions[unions[i]]
        i = unions[i]        
    return (i)


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
routes = []
for route_i in range(m):
   routes.append([int(aroute) for aroute in input().strip().split(' ')])    
    
unions = [id for id in range(n)]
for route in routes:
    pid = root(route[0] - 1)
    qid = root(route[1] - 1)
    unions[pid] = qid
       
roots = [root(i) for i in unions]
groups = [len(list(group)) for key, group in itertools.groupby(sorted(roots))]

print(max(groups))
    


