from aoc_util.advent import Input
import itertools as it
from collections import Counter
from queue import PriorityQueue
from functools import reduce
import math
import sys
from z3 import *

def get_all_points(p1, p2):
    return it.product(*zip(list(p1), list(p2)))

def parse(l: list[str]) -> list[tuple[int]]:
    import re

    bots = []
    for item in l:
        bots.append(tuple(map(int, re.findall(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', item)[0])))
    return bots

def in_range(point, bots):
    return any(b[-1] >= sum(abs(x - y) for x,y in zip(point, b)) for b in bots)

def get_next(m, M):
    mid = tuple([(x + y) // 2 for x,y in zip(list(m), list(M))])
    new_start_points = [x for x in sorted(get_all_points(m, mid))]
    new_end_points = [x for x in sorted(get_all_points(mid, M))]
    return list(zip(new_start_points, new_end_points))

def p2(day: Input):
    bots = parse(day.lines())
    min_radius = min(bots, key=lambda b: b[-1])[-1]
    min_points = [min(bots, key=lambda b: b[i])[i] for i in range(3)]
    max_points = [max(bots, key=lambda b: b[i])[i] for i in range(3)]

    Q = [(tuple(min_points), tuple(max_points))]
    max_points = 0
    while min_radius > 1:
        points_in_range = []
        while Q:
            m, M = Q.pop(0)
            points = list(get_all_points(m, M))
            print(len(Q))

            if not any(in_range(p, bots) for p in points):
                if not any(all(m[i] <= b[i] <= M[i] for i in range(3)) for b in bots):
                    continue

            mp = [(sum(int(b[-1] >= sum(abs(x-y) for x,y in zip(p,b))) for b in bots), p) for p in points]

            if min_radius == 3 and sum(abs(m[i] - M[i]) for i in range(3)) == min_radius:
                points_in_range.append((max(mp), (m,M)))
                continue

            if max(mp)[0] < max_points: continue

            if max_points < max(mp)[0]:
                max_points = max(mp)[0]

            if all(abs(m[i] - M[i]) < min_radius for i in range(3)): #abs(m[0] - M[0]) < min_radius:
                points_in_range.append((max(mp), (m,M)))
                continue

            Q += get_next(m, M)


        min_points = []

        for val, cube in points_in_range:
            if val[0] == max_points:
                if min_radius == 3:
                    min_points.append(
                        min([
                            p for p in get_all_points(*cube)
                            if sum(int(b[-1] >= sum(abs(x-y) for x,y in zip(p,b))) for b in bots) == max_points
                        ], key=lambda x: sum(abs(xx) for xx in x))
                    )
                    continue
                next_cubes = get_next(*cube)
                Q += next_cubes

        if min_radius == 3:
            return min(sum(abs(xx) for xx in x) for x in min_points)
        min_radius = max(3, min_radius // 2)
