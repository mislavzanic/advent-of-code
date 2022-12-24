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
from advent import Input

day = Input()
# day = Input('input/21.ex')

d = defaultdict(str)
for item in day.lines:
	items = item.split(': ')
    d[items[0]] = items[1]


def dp(curr, part):
	expr = d[curr]
	if expr.isdigit():
		# if part == '2':
		#     if curr != 'humn':
		#         return int(expr)
		#     return curr
		return int(expr)
	else:
		a, op, b = expr.split(' ')
		n1 = dp(a,part)
		n2 = dp(b,part)
		if curr == 'root' and part == '2': op = '-'
		if isinstance(n1, int)  and isinstance(n2, int):
			return int(eval(str(n1) + op + str(n2)))
		# if op in ['+', '-']:
		#     return str(n1) + op + str(n2)
		return '(' + str(n1) + op + str(n2) + ')'


expr = dp('root', '1')
print(expr)
M = 100000000000000000000
m = 0
while M != m:
	middle = (M + m) // 2
	print(middle)
	d['humn'] = str(middle)
	expr = int(dp('root', '2'))
	print(expr, d['humn'])
	if expr < 0: M = middle
	elif expr == 0:
		print(middle - 1)
		break
	else: m = middle

# expr = dp('root', '2')[1:-1].split('=')
# print(expr[0][1:-1], expr[1])
# for key in d.keys():
#     if key in expr and key != 'humn':
#         expr = expr.replace(key, d[key])
#     if key == 'humn':
#         expr = expr.replace(key, 'x')

# sympy_eq = sympy.sympify(expr)
# res = sympy.solvers.solve(sympy_eq, sympy.Symbol('x'))[0]
# print(res)
