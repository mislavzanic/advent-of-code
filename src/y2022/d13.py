#!/usr/bin/env python3

from get_input import get_aoc_input
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math


def parse(example=''):
    if example == '':
        with get_aoc_input(13, 2022) as f:
            return [x.split('\n') for x in f.read().split('\n\n')]
    return [x.split('\n') for x in open(example).read().split('\n\n')]


def compare(l,r):
    if isinstance(l,int) and isinstance(r,int):
        if l > r: return 1
        if l < r: return -1
        else: return 0
    elif isinstance(l,int) and isinstance(r,list):
        return compare([l],r)
    elif isinstance(l,list) and isinstance(r,int):
        return compare(l,[r])
    elif isinstance(l, list) and isinstance(r,list):
        for i, item in enumerate(l):
            if i < len(r):
                c = compare(item, r[i])
                if c != 0:
                    return c
            else:
                return 1
        if len(l) < len(r): return -1
        return 0


ll = parse()
s = 0
packets = []
for i, item in enumerate(ll):
    l,r = list(map(ast.literal_eval, item))
    packets.append(l)
    packets.append(r)
    if compare(l,r) == -1:
        s += i + 1

print(s)

packets.append([[2]])
packets.append([[6]])
sorted_p = sorted(packets, key=functools.cmp_to_key(lambda x,y: compare(x,y)))

p = 1
for i,item in enumerate(sorted_p):
    if item == [[2]] or item == [[6]]:
        p *= (i + 1)

print(p)
