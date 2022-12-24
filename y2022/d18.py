#!/usr/bin/env python3

from typing import get_origin
# from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math
from advent import Input

day = Input(18,2022)
ll = day.lines

cubes = set(tuple(map(int, item.split(','))) for item in ll)

X, Y, Z = max(cubes,key=lambda x: x[0])[0] ,max(cubes,key=lambda x: x[1])[1] ,max(cubes,key=lambda x: x[2])[2]
x, y, z = min(cubes,key=lambda x: x[0])[0] ,min(cubes,key=lambda x: x[1])[1] ,min(cubes,key=lambda x: x[2])[2]

air = set()
new_cubes = set()

def fill(cube, cubes, air, new_cubes):
    global X, Y, Z, x, y, z, SEEN
    stack = [cube]
    seen = set()
    while len(stack) > 0:
        curr = stack.pop(0)
        SEEN.add(curr)
        if curr in seen: continue
        seen.add(curr)
        if curr in cubes: continue
        if curr in air:
            for item in seen:
                if item not in cubes:
                    air.add(item)
            return False
        if curr in new_cubes:
            for item in seen:
                if item not in cubes:
                    new_cubes.add(item)
            return True
        if x <= curr[0] <= X and y <= curr[1] <= Y and z <= curr[2] <= Z:
            for n in [-1,1]:
                i,j,k = curr[0], curr[1], curr[2]
                stack.append((i+n,j,k))
                stack.append((i,j+n,k))
                stack.append((i,j,k+n))
        else:
            for item in seen:
                if item not in cubes:
                    air.add(item)
            return False
    for item in seen:
        if item not in cubes:
            new_cubes.add(item)
    return True


SEEN = set(c for c in cubes)
for i in range(x, X+1):
    for j in range(y, Y+1):
        for k in range(z, Z+1):
            if (i,j,k) not in SEEN:
                fill((i,j,k),cubes,air,new_cubes)

def area(cubes):
    d = Counter()
    for i,c1 in enumerate(cubes):
        for j,c2 in enumerate(cubes):
            if i == j: continue
            s = sum(abs(s1-s2) for (s1,s2) in zip(c1,c2))
            if s == 1 and (tuple(c1),tuple(c2)) not in d.keys():
                d[(tuple(c1), tuple(c2))] += 1
                d[(tuple(c2), tuple(c1))] += 1

    return len(cubes) * 6 - sum(d.values())

a = area(cubes)
print(a)
print(a - area(new_cubes))
