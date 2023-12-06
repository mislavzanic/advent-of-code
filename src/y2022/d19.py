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
        with get_aoc_input(19, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open(example).readlines()]

def collect(r, ore):
    for k,v in r.items():
        ore[k] += v


def build(costs, ore):
    robots = []
    for robot,cost in costs.items():
        ok = True
        for k,v in cost.items():
            if ore[k] < v:
                ok = False
                break
        if ok: robots.append(robot)
    return robots

def add_robot(robot, stack, curr_robots, ore, time):
    new_robots = {k:v + int(k == robot) for (k,v) in curr_robots.items()}
    new_ore = {k:v for k,v in ore.items()}

    for k,v in costs[robot].items():
        new_ore[k] -= v
    stack.append((new_robots, new_ore, time - 1))

ll = parse()
# ll = parse('input/19.ex')

bp = []

for item in ll:
    m = re.findall(r'Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', item)
    m = list(map(int, m[0]))
    bp.append([{'ore': m[0]}, {'ore':m[1]}, {'ore': m[2],'clay':m[3]}, {'ore':m[4],'obsidian':m[5]}])


keys = ['ore', 'clay', 'obsidian', 'geode']
s = []
for i,item in enumerate(bp):
    if i == 3: break
    M = 0
    costs = {k:v for (k,v) in zip(keys, item)}
    robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    ore = {k:0 for k in keys}

    ore_cap = {k:0 for k in keys}
    for k,v in costs.items():
        for kk,vv in v.items():
            if ore_cap[kk] < vv:
                ore_cap[kk] = vv
    ore_cap['geode'] = 1000000000

    TIME = 32

    stack = [(robots, ore, TIME)]
    SEEN = set()

    while len(stack) > 0:
        curr_robots, ore, time = stack.pop()

        prune = False
        for v1,v2 in zip(ore.values(), ore_cap.values()):
            if v1 > 5 * v2:
                prune = True
                break

        if prune: continue

        if TIME // 2 >= time:
            l = list(k for k,v in ore.items() if v != 0)
            if len(l) == 1 and 'geode' not in l:
                continue

        if time == 0:
            print(M)
            M = max(M, ore['geode'])
            continue

        if time == 1 and curr_robots['geode'] + ore['geode'] <= M:
            continue

        if time == 2 and 2 * curr_robots['geode'] + ore['geode'] + 1 <= M:
            continue

        if time == 3 and 3 * curr_robots['geode'] + ore['geode'] + 3 <= M:
            continue


        if (time,tuple(ore.values()),tuple(curr_robots.values())) in SEEN:
            continue
        SEEN.add((time,tuple(ore.values()), tuple(curr_robots.values())))

        possible_robots = build(costs, ore)
        collect(curr_robots, ore)

		if 'geode' in possible_robots and time >= 2:
			add_robot('geode', stack, curr_robots, ore, time)
		else:
			if time > 2:
				if 'obsidian' in possible_robots:
					possible_robots.remove('obsidian')
					possible_robots = ['obsidian'] + possible_robots
				for robot in possible_robots:
					if ore_cap[robot] > curr_robots[robot]:
						add_robot(robot, stack, curr_robots, ore, time)
			stack.append((curr_robots, ore, time - 1))
	s.append(M)
	print(M,i)

print(functools.reduce(lambda a,b: a*b, s))
