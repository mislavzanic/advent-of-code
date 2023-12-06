#!/usr/bin/env python3

from get_input import get_aoc_input
import itertools as it
from collections import Counter, defaultdict

def parse(example=''):
    if example == '':
        with get_aoc_input(16, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open(example).readlines()]


ll = parse()
ll = parse('input/16.ex')

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

def dp(points, time):
    global memoise

    points = tuple(sorted(list(points)))

    if points in memoise.keys():
        return memoise[points]

    # if len(points) == 5:
    #     score = 0
    #     state = (0,None,0)
    #     for perm in it.permutations(points):
    #         ns = calc_score(perm, time)
    #         if ns > score:
    #             score = ns
    #             state = (ns, )
    #         ...

    if len(points) == 1:
        point = list(points)[0]
        time_left = time - 1 - pipe_map['AA'][point]
        memoise[points] = (time_left * rates[point], points, time_left)
        return memoise[points]

    score = 0
    state = (0, None, 0)
    for subset in it.combinations(points, len(points) - 1):
        sub_score, path, time_left = dp(subset, time)
        next_point = list(set(points) - set(subset))[0]
        time_left -= (pipe_map[path[-1]][next_point] + 1)
        if time_left > 0:
            sub_score += time_left * rates[next_point]
        if sub_score > score:
            score = sub_score
            state = (score, tuple(list(path) + [next_point]), time_left)
    memoise[points] = state
    return state

all_points = pipe_map.keys() - {'AA'}
state = dp(all_points, 30)
print(state[0])
memoise.clear()

state = dp(all_points, 26)

M = 0
path = None

for key in memoise.keys():
    rest = sorted(list(all_points - set(key)))
    if rest == []: continue
    if rest == ["DD", "EE", 'HH']:
        print(memoise[tuple(rest)])
        print(memoise[key])
    if key == ('BB','JJ'):
        print(memoise[key])
        print((26 - 1 -pipe_map['AA']['JJ']) * rates['JJ'] + rates['BB'] * (26 - 2- pipe_map['AA']['JJ'] - pipe_map['JJ']['BB']), ('JJ','BB'))
    if M < memoise[key][0] + memoise[tuple(rest)][0]:
        M = max(M, memoise[key][0] + memoise[tuple(rest)][0])
        path = (memoise[key], memoise[tuple(rest)])
print(M,path)
