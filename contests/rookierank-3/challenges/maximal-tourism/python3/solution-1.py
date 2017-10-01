

#!/bin/python3

import sys
import itertools


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
routes = []
for route_i in range(m):
   routes.append([int(aroute) for aroute in input().strip().split(' ')])
    
unions = [id for id in range(n)]
for route in routes:
    pid = unions[route[0] - 1]
    qid = unions[route[1] - 1]    
    for position in range(n):
        unions[position] = qid if unions[position] == pid else unions[position]
       
groups = [len(list(group)) for key, group in itertools.groupby(sorted(unions))]
print(max(groups))


