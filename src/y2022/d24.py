import collections
from typing import get_origin
# from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math
from aoc_util.advent import Input
import aoc_util.utils

def blizzard_move(bl_pos):
	global blizzard, X, Y

	bp = []

	for i,item in enumerate(bl_pos):
		direction, coord = item
		nx, ny = coord[0] + blizzard[direction][0], coord[1] + blizzard[direction][1]

		if nx == 0: nx = X - 2
		if ny == 0: ny = Y - 2
		if nx == X - 1: nx = 1
		if ny == Y - 1: ny = 1

		bp.append((direction, (nx, ny)))

	return bp

day = Input(day=24, year=2022)

blizzard = {'>': (0,1), '^':(-1,0), 'v':(1,0), '<':(0,-1)}
bl = []
wall = []
lines = day.lines()
end = (len(lines) - 1, len(lines[-1]) - 2)
X, Y = len(lines), len(lines[-1])
for i,line in enumerate(lines):
	for j, char in enumerate(line):
		if char == '#': wall.append((i,j))
		if char in '<>^v': bl.append((char, (i,j)))

start_bl = [x for x in bl]
start = (0,1)
# Q = [(start, 0, start_bl)]

blizzards = [start_bl]
period = 0
while True:
	bl = blizzard_move(bl)
	period += 1
	if sorted(list(bl)) == sorted(start_bl): break
	blizzards.append([x for x in bl])

def callback(M):
        global period, wall, blizzards
        def find_next(curr):
                pos, minute = curr
                cx, cy = pos
                bl = blizzards[(M + minute + 1) % period]
                bl_pos = [x[1] for x in bl]
                next_moves = []
                for move in [(-1,0), (1,0), (0,-1), (0,1), (0,0)]:
                        x,y = move
                        if (cx + x, cy + y) in bl_pos + wall: continue
                        if 0 <= cx + x < X and 0 <= cy + y < Y:
                                next_moves.append(((cx + x, cy + y), minute + 1))
                return next_moves
        return find_next

def _bfs(start, end, M):
    global period, wall, blizzards
    path = aoc_util.utils.bfs([(start, 0)], end, lambda x: x[0] == end, callback(M), lambda x: (x[0], x[1] % period))
    assert path != None, "No Path"
    l = [end]
    curr = end
    for v in path.values():
            for item in v:
                    if item[0] == end:
                            return item[1]
    return None

M = _bfs(start, end, 0)
print(M)
M1 = _bfs(end, start, M)
M2 = _bfs(start, end, M + M1)
print(M + M1 + M2)
