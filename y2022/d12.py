#!/usr/bin/env python3

from get_input import get_aoc_input
import itertools as it
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import math


def parse(example=''):
    if example == '':
        with get_aoc_input(12, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open('input/12.ex').readlines()]




d = defaultdict(str)
ll = parse()
ll = parse('input/12.ex')
start, goal = [], (0,0)
for i, row in enumerate(ll):
    for j, col in enumerate(row):
        d[(i,j)] = col
        if col == 'S' or col == 'a':
            if col == 'S': start = [(i,j)] + start
            else: start.append((i,j))
        if col == 'E': goal = (i,j)


steps = set()
currMin = -1
for item in start:
    stack, seen = [(item, 0)], set()
    while len(stack) > 0:
        curr, step = stack.pop(0)
        if step >= currMin and currMin > 0: continue
        f = False
        if curr in seen: continue
        if d[curr] == 'E':
            print(step)
            if currMin < 0 or currMin > step:
                currMin = step
            break
        seen.add(curr)
        neighbors = [(i,j) for i in [-1, 0, 1] for j in [-1,0,1] if i != j and i * j == 0]
        for dp in neighbors:
            n = (curr[0] + dp[0], curr[1] + dp[1])
            if d[n] != '' and (ord(d[n]) - ord(d[curr]) <= 1 or d[curr] == 'S' or d[n] == 'E'):
                if d[n] == 'E' and d[curr] != 'z': continue
                stack.append((n, step + 1))

print(currMin)
