import fileinput
import re
from collections import deque

p1 = [0 for _ in range(4)]
wp1 = 0
p2 = [0 for _ in range(4)]
wp2 = deque([10, 0, 0, 1])

dirs = {'E':0, 'S':1, 'W':2, 'N':3}
lines = [x for x in list(fileinput.input())]
for line in lines:
    d = line.strip()[0]
    num = int(re.findall('-?\d+', line)[0])
    if d == 'F':
        p1[wp1] += num
        for i in range(4):
            p2[i] += num*wp2[i]
    elif d in dirs.keys():
        p1[dirs[d]] += num
        wp2[dirs[d]] += num
    elif d == 'L':
        m = num//90
        wp1 = (wp1 - m) % 4
        wp2.rotate(-m)
    else:
        m = num//90
        wp1 = (wp1 + m) % 4
        wp2.rotate(m)
print(abs(p1[1] - p1[3]) + abs(p1[0] - p1[2]))
print(abs(p2[1] - p2[3]) + abs(p2[0] - p2[2]))
