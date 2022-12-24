#!/usr/bin/env python3

from typing import get_origin
from get_input import get_aoc_input
# from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math

def parse(example=''):
    if example == '':
        with get_aoc_input(17, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open(example).readlines()]

ll = parse()[0]
N = 1000000000000

period = len(ll) * 5

def rock_height(rock):
    return len(rock.split(';'))

def rock_width(rock):
    return len(rock.split(';')[0])

def fill_in(curr_rock, d):
    for x in range(len(curr_rock)):
        for y in range(len(curr_rock[0])):
            ww,hh = curr_rock[x][y]
            if ww == -1 and hh == -1: continue
            d[(ww,hh)] = '#'

def get_rock(rock, curr_height):
    r = rock.split(';')
    s = [[(-1,-1)if r[j][i] == '.' else (2 + i, curr_height + rock_height(rock) - j - 1) for i in range(rock_width(rock))] for j in range(rock_height(rock))]
    return reversed(s)

def get_edge(curr_rock, direction):
    arr = []
    for row in curr_rock:
        for col in row:
            if direction[0] == 0 and col[1] > -1: arr.append(col[1])
            if direction[1] == 0 and col[1] > -1: arr.append(col[0])

    if sum(direction) == 1: return max(arr)
    return min(arr)

def get_leftmost(curr_rock):
    return get_edge(curr_rock, (-1,0))

def get_rightmost(curr_rock):
    return get_edge(curr_rock, (1,0))

def get_highest(curr_rock):
    return get_edge(curr_rock, (0,1))

def get_lowest(curr_rock):
    return get_edge(curr_rock, (0,-1))

def move(direction, curr_rock, d):
    leftmost, rightmost = get_leftmost(curr_rock), get_rightmost(curr_rock)
    for i,slab in enumerate(curr_rock):
        for j,part in enumerate(slab):
            w,h = part
            if w == -1 and h == -1: continue
            if d[(w+direction[0],h+direction[1])] == '#': return False

    if (leftmost == 0 and direction[0] == -1) or (rightmost == 6 and direction[0] == 1): return False

    for i,slab in enumerate(curr_rock):
        for j,part in enumerate(slab):
            w,h = part
            if w == -1 and h == -1: continue
            curr_rock[i][j] = (w + direction[0], h + direction[1])
    return True

ll = list(ll)
diff,rocks_height= [],[0]

rocks = [
    '####',
    '.#.;###;.#.',
    '..#;..#;###',
    '#;#;#;#',
    '##;##'
]

d = defaultdict(str)
width = 7
curr_height = 3
idx = 0
fallen = [0]
for i in range(width):
    d[(i,-1)] = '#'
for i in range(period):
    curr_rock = list(get_rock(rocks[i % 5], curr_height))
    if idx == 0 and i != 0:
        fallen.append(i)
    while True:
        c = ll[idx]
        idx = (idx + 1) % len(ll)
        if c == '<':
            move((-1,0), curr_rock, d)
        else:
            move((1,0), curr_rock, d)

        bottom = move((0,-1), curr_rock, d)

        if not bottom:
            fill_in(curr_rock, d)
            rocks_height.append(get_highest(curr_rock) + 1)
            curr_height = max([curr_height, get_highest(curr_rock) + 3 + 1])
            break

r = fallen[2] - fallen[1]
print(rocks_height[2022])
print(rocks_height[fallen[1]] + ((N - fallen[1]) // (r)) * (rocks_height[fallen[2]] - rocks_height[fallen[1]]) + rocks_height[((N - fallen[1]) % (r)) + fallen[1]] - rocks_height[fallen[1]])
