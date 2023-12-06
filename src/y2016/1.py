from collections import defaultdict
import sys

d = defaultdict(int)

path = open('input').readline().strip().split(', ')
dir_ = 0
DX = [0,1,0,-1]
DY = [1,0,-1,0]
num = [0, 0]
found = False
for p in path:
    r = int(p[1:])
    if p[0] == 'R':
        dir_ += 1
    else:
        dir_ -= 1
    dir_ %= 4
    for i in range(r):
        num[0] += DY[dir_]
        num[1] += DX[dir_]
        d[tuple(num)] += 1
        if d[tuple(num)] == 2 and not found:
            found = True
            print(abs(num[0]) + abs(num[1]))
print(abs(num[0]) + abs(num[1]))


