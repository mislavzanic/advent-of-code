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
# day = Input('input/22.ex')

grid, path = day.string.split('\n\n')
grid = grid.split('\n')

facing = {'R':0, 'D':1, 'L':2, 'U':3}

faces = [
	{'R':(1,'R'), 'D':(2,'D'), 'L':(3,'R'), 'U':(5,'R')},
	{'R':(4,'L'), 'D':(2,'L'), 'L':(0,'L'), 'U':(5,'U')},
	{'R':(1,'U'), 'D':(4,'D'), 'L':(3,'D'), 'U':(0,'U')},
	{'R':(4,'R'), 'D':(5,'D'), 'L':(0,'R'), 'U':(2,'R')},
	{'R':(1,'L'), 'D':(5,'L'), 'L':(3,'L'), 'U':(2,'U')},
	{'R':(4,'U'), 'D':(1,'D'), 'L':(0,'D'), 'U':(3,'U')},
]
# faces = [
# 	{'R':(5,'L'), 'D':(3,'D'), 'L':(2,'D'), 'U':(1,'D')},
# 	{'R':(2,'R'), 'D':(4,'U'), 'L':(5,'U'), 'U':(0,'D')},
# 	{'R':(3,'R'), 'D':(4,'R'), 'L':(1,'L'), 'U':(0,'R')},
# 	{'R':(5,'D'), 'D':(4,'D'), 'L':(2,'L'), 'U':(0,'U')},
# 	{'R':(5,'R'), 'D':(1,'U'), 'L':(2,'U'), 'U':(3,'U')},
# 	{'R':(0,'L'), 'D':(1,'R'), 'L':(4,'L'), 'U':(3,'L')},
# ]
N = 50
cube_faces = [defaultdict(str) for _ in range(6)]
d = defaultdict(str)
dir_map = {'U': (-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
faces_adjust = {0: (0,-50), 1: (0, -100), 2:(-50,-50), 3:(-100,0), 4:(-100,-50), 5:(-150,0)}
# faces_adjust = {0: (0,-8), 1: (-4, 0), 2:(-4,-4), 3:(-4,-8), 4:(-8,-8), 5:(-8,-12)}
r_map = {'U':'R', 'R':'D', 'D':'L','L':'U'}
l_map = {v:k for k,v in r_map.items()}

def rotate(point, curr_dir, new_dir):
	print(f"start: {point}, {curr_dir}, {new_dir}")
	global r_map, dir_map, N
	while curr_dir != new_dir:
		curr_dir = r_map[curr_dir]
		point = (point[1], N - 1 - point[0])
	print(f"end: {point}, {curr_dir}, {new_dir}")
	return point

def move_in_dir(curr_pos, curr_dir, cube_face, dist):
	# print(curr_pos, curr_dir, cube_face, dist)
	global d, dir_map, faces, faces_adjust, cube_faces
	opposite = {k:r_map[r_map[k]] for k in 'UDLR'}
	cx, cy = curr_pos
	field = []

	if curr_dir in 'LR':
		field = [x for x in cube_faces[cube_face].keys() if cx == x[0]]
	else:
		field = [x for x in cube_faces[cube_face].keys() if cy == x[1]]

	assert len(field) == N and field == sorted(field), (field, len(field), curr_pos, cube_face)

	# print(field)
	idx = field.index(curr_pos)
	for i in range(1, dist + 1):
		new_pos = curr_pos

		if (idx + i == N and curr_dir in 'DR') or (idx - i == -1 and curr_dir in 'LU'):
			new_cube_face, new_dir = faces[cube_face][curr_dir]
			new_pos = rotate((
				(curr_pos[0] + faces_adjust[cube_face][0] + dir_map[curr_dir][0]) % N,
				(curr_pos[1] + faces_adjust[cube_face][1] + dir_map[curr_dir][1]) % N
			), opposite[curr_dir], opposite[new_dir])
			new_pos = (
				new_pos[0] - faces_adjust[new_cube_face][0],
				new_pos[1] - faces_adjust[new_cube_face][1]
			)
			assert new_pos in d.keys()
			if d[new_pos] == '#': break
			d[new_pos] = new_dir
			return move_in_dir(new_pos, new_dir, new_cube_face, dist - i)
		else:
			new_pos = field[idx - i] if curr_dir in 'LU' else field[idx + i]

		if d[new_pos] == '#': break
		assert d[new_pos] != '' and cube_faces[cube_face][new_pos] != '', (new_pos)

		d[new_pos] = curr_dir
		curr_pos = new_pos
	return curr_pos, curr_dir, cube_face

for i,line in enumerate(grid):
	for j,char in enumerate(line):
		if char == ' ': continue
		# if i < 4 and 8 <= j < 12:
		# 	cube_faces[0][(i,j)] = char
		# if 4 <= i < 8:
		# 	cube_faces[1 + ( j // 4 )][(i,j)] = char
		# if i >= 8:
		# 	cube_faces[2 + ( j // 4 )][(i,j)] = char
		# 	print(2 + (j // 4), i, j)
		if i < 50:
			cube_faces[(j // 50) - 1][(i,j)] = char
		if 50 <= i < 100:
			cube_faces[2][(i,j)] = char
		if 100 <= i < 150:
			cube_faces[3 + (j // 50)][(i,j)] = char
		if i >= 150:
			cube_faces[5][(i,j)] = char
		d[(i,j)] = char


path = 'L,'.join(path.split('L'))
path = 'R,'.join(path.split('R'))
path = path.split(',')

curr_pos, curr_dir, curr_face = min([x for x in d.keys() if x[0] == 0], key=lambda x: x[1]), 'R', 0

final_dir = ''
for p in path:
	p = p.strip()
	if p.isnumeric():
		curr_pos, curr_dir, curr_face = move_in_dir(curr_pos, curr_dir, curr_face, int(p))
	else:
		dist,rot = int(p[:-1]), p[-1]
		curr_pos, curr_dir, curr_face = move_in_dir(curr_pos, curr_dir, curr_face, int(dist))
		if rot == 'L':
			curr_dir = l_map[curr_dir]
		else:
			curr_dir = r_map[curr_dir]
	# for i in range(len(grid)):
	# 	s = ''
	# 	for j in range(len(grid[i])):
	# 		if (i,j) in d.keys():
	# 			s += d[(i, j)]
	# 		else: s += ' '
	# 	print(s)

	# print(f'---------- {curr_pos}, {curr_dir}, {curr_face}')
print((1000 * (curr_pos[0] + 1)) + (4 * (curr_pos[1] + 1)) + facing[curr_dir])
day.submit((1000 * (curr_pos[0] + 1)) + (4 * (curr_pos[1] + 1)) + facing[curr_dir], 2)
