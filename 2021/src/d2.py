import re
import itertools
from collections import defaultdict

def part2(inlist):
    d = defaultdict(int)
    for l in inlist:
        l = l.split()
        if l[0] == "forward":
            d[0] += int(l[1])
            d[1] += d[2] * int(l[1])
        elif l[0] == 'down':
            d[2] += int(l[1])
        else:
            d[2] -= int(l[1])
    return d[0] * d[1]

def part1(inlist):
    d = defaultdict(int)
    for l in inlist:
        l = l.split()
        if l[0] == "forward":
            d[0] += int(l[1])
        elif l[0] == 'down':
            d[1] += int(l[1])
        else:
            d[1] -= int(l[1])
    return d[0] * d[1]
