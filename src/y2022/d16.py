#!/usr/bin/env python3

import functools
from sympy import functions
from advent import Input
import itertools as it
from collections import Counter, defaultdict


def get_score(path, time):
    global pipe_map, rates
    score = 0
    for i in range(1, len(path)):
        score += (time - 1 - pipe_map[path[i-1]][path[i]]) * rates[path[i]]
        time -= 1
    return score


day = Input('input/16.in')
ll = day.lines

leads_to = defaultdict(tuple)
rates = Counter()
for item in ll:
    items = item.split('; ')
    rate = int(items[0].split('=')[1])
    start = items[0].split(' ')[1]
    valves = items[1].split(', ')
    valves[0] = valves[0].split(' ')[-1]
    rates[start] = rate
    leads_to[start] = tuple(valves)

def get_steps(start, end, leads_to):
    stack = [(start, 0)]
    seen = set()
    while len(stack) > 0:
        curr,steps = stack.pop(0)
        if curr in seen: continue
        if curr == end:
            return steps
        seen.add(curr)
        for n in leads_to[curr]:
            stack.append((n,steps + 1))
    return None

pipe_map = defaultdict(Counter)
for k1 in rates.keys():
    for k2 in rates.keys():
        if k1 != k2 and ((k2 == 'AA' and rates[k1] != 0) or (rates[k1] != 0 and rates[k2] != 0)):
            steps = get_steps(k1, k2, leads_to)
            if pipe_map[k2][k1] > steps or pipe_map[k2][k1] == 0:
                pipe_map[k2][k1] = steps
            if pipe_map[k1][k2] > steps or pipe_map[k2][k1] == 0:
                pipe_map[k1][k2] = steps


memoise = defaultdict(tuple)

@functools.lru_cache(maxsize=None)
def dfs1(t, curr, rest):
    global pipe_map
    if t == 0 or len(rest) == 0:
        return 0
    if len(rest) == 1:
        return rates[rest[0]] * (t - 1 - pipe_map[curr][rest[0]])

    flow = rates[curr]
    return max([0] + [
        rates[n] * (t - 1 - pipe_map[curr][n]) + dfs1(t - 1 - pipe_map[curr][n], n, tuple([r for r in rest if r != n]))
        for n in rest
        if t > 1 + pipe_map[curr][n]
    ])

def dfs2(points):
    max_score = 0
    for l in range(1, len(points) // 2):
        for comb in it.combinations(points,l):
            max_score = max(max_score, dfs1(26, 'AA', tuple(sorted(comb))) + dfs1(26, 'AA', tuple(sorted([p for p in points if p not in comb]))))
    return max_score

# print(dfs1(30, 'AA', tuple(sorted((pipe_map.keys() - {'AA'}))))) part 1
print(dfs2(tuple(sorted((pipe_map.keys() - {'AA'})))))
