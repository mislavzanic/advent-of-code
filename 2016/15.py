from collections import defaultdict
from collections import deque
import sys

l = [x.strip() for x in open('input').readlines()]
discs = []
for x in l:
    x = x.split()
    num, numpos, pos = int(x[1][1:]), int(x[3]), int(x[-1][:-1])
    discs.append([num, numpos, pos])
p1 = 0
time = 0
for i in range(2):
    time = 0
    while True:
        found = False
        for d in discs:
            num, numpos, pos = d
            pos = (pos + time + num) % numpos
            if pos != 0:
                found = True
                time += 1
                break
        if not found:
            p1 = time
            print(p1)
            break
    discs.append([7,11,0])    
