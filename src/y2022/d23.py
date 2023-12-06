import collections
from typing import get_origin
import sympy
# from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math
from aoc_util.advent import Input

day = Input()

d = defaultdict(str)
for i,line in enumerate(day.lines):
	for j,char in enumerate(line):
		d[(i,j)] = char


choices = ['N', 'S', 'W', 'E']
dirs = {
	'N': tuple([(-1,0), (-1,-1), (-1,1)]),
	'S': tuple([(1,0), (1,-1), (1,1)]),
	'W': tuple([(0,-1), (-1,-1), (1,-1)]),
	'E': tuple([(0,1), (-1,1), (1,1)]),
}

for i in range(100000):
	new_directions = defaultdict()
	for key in list(d.keys()):
		if d[key] != '#': continue

		if all(d[key[0]+x[0],key[1]+x[1]] != '#' for x in [(-1,0), (-1,-1), (-1,1), (1,0), (1,-1), (1,1), (0,-1), (0,1)]):
			continue

		for choice in choices:
			if all([d[(key[0] + x[0], key[1]+x[1])] != '#' for x in dirs[choice]]):
				new_directions[key] = dirs[choice][0]
				break

	new_pos = [(k,(k[0] + v[0], k[1] + v[1])) for k,v in new_directions.items()]

	for elf, pos in new_pos: assert d[elf] == '#' and d[pos] != '#', (elf, pos, d[elf], d[pos], new_pos)

	moved = False

	while len(new_pos) > 0:
		elf, pos = new_pos.pop()

		assert d[elf] == '#' and d[pos] != '#', (elf,pos,d[elf],d[pos])

		removed = False
		for e, pos2 in new_pos:
			if pos == pos2:
				removed = True
				new_pos.remove((e,pos2))

		if removed: continue

		d[elf] = '.'
		d[pos] = '#'
		moved = True
	choices.append(choices.pop(0))
	if i == 9:
		mx, MX = min([x for x in d.keys() if d[x] == '#'], key=lambda x: x[0])[0], max([x for x in d.keys() if d[x] == '#'], key=lambda x: x[0])[0]
		my, MY = min([x for x in d.keys() if d[x] == '#'], key=lambda x: x[1])[1], max([x for x in d.keys() if d[x] == '#'], key=lambda x: x[1])[1]

		s = 0
		for i in range(mx, MX + 1):
			for j in range(my, MY + 1):
				s += d[(i,j)] != '#'
		# day.submit(s, 1)
		print(s)

	if not moved:
		# day.submit(i+1, 2)
		print(i+1)
		break


