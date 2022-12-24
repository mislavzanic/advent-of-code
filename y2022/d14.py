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
        with get_aoc_input(14, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open(example).readlines()]

def move_down(d, sand, floor):
    x,y = sand
    if y+1 == floor:
        return (x,y)
    if d[(x,y+1)] == '':
        return (x,y+1)
    if d[(x-1,y+1)] == '':
        return (x-1,y+1)
    if d[(x+1,y+1)] == '':
        return (x+1,y+1)
    return (x,y)

def fall(d, sand, floor, p1):
    while True:
        new_sand = move_down(d,sand,floor)
        if p1:
            if new_sand[1] > floor - 2:
                print(len([v for v in d.values() if v == 'o']))
                p1 = False
        if new_sand == sand:
            return sand, p1
        sand = new_sand


ll = parse()
S = (500, 0)
d = defaultdict(str)

d[S] = '+'
MY = -1
for item in ll:
    l = [tuple(map(int, x.split(','))) for x in item.split(' -> ')]
    for i in range(len(l) - 1):
        start, end = l[i],l[i+1]
        mx, Mx = sorted([start[0], end[0]])
        my, My = sorted([start[0], end[0]])
        if MY <= My: MY = My
        for x in range(mx, Mx+1):
            for y in range(my, My+1):
                d[(x,y)] = '#'


p1 = True
while True:
    sand,p1 = fall(d,(500,0),MY+2,p1)
    if sand == (500,0):
        d[(500,0)] = 'o'
        print(len([k for k,v in d.items() if v == 'o']))
        break
    d[sand] = 'o'
