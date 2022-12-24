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
# day = Input(input_str='input/25.ex')

M = {'=': -2, '-': -1, '0':0, '1':1, '2':2}
def number(line):
	global M
	p = 0
	n = 0
	for char in line:
		n = 5 * n + M[char]
		p += 1
	return n

def to_b5(num):
	global M
	s = ''
	m = {v:k for k,v in M.items()}
	while num:
		for i in range(-2, 3):
			if (num - i) % 5 == 0:
				num -= i
				s += m[i]
				num /= 5
				break
	return s

s = 0
print(number('2=-01'))
for line in day.lines:
	s += number(line)

print(s,''.join(list(reversed(to_b5(s)))))
