#!/usr/bin/env python3

from get_input import get_aoc_input
from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math

def in_range(beacon):
    return 0 <= beacon[0] <= 4000000 and 0 <= beacon[1] <= 4000000

def parse(example=''):
    if example == '':
        with get_aoc_input(15, 2022) as f:
            return [x.strip() for x in f.readlines()]
    return [x.strip() for x in open(example).readlines()]

def manh_d(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

ll = parse()

sensors, beacons = set(), set()
closest = defaultdict(tuple)
for line in ll:
    m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    if m is not None:
        sensor = tuple([int(m[1]), int(m[2])])
        beacon = tuple([int(m[3]), int(m[4])])
        sensors.add(sensor)
        beacons.add(beacon)

m, M = 0, 4000000
y = 2000000

for sensor in sensors:
    md = None
    for beacon in beacons:
        if md is None or manh_d(sensor, beacon) < md:
            closest[sensor] = (beacon, manh_d(sensor, beacon))
            md = manh_d(sensor, beacon)

def zabs(x) -> Tactic:
    return If(x >= 0, x, -x)


def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
    return arr, index


def get_intervals(y, closest):
    intervals = []
    for k,v in closest.items():
        dy = abs(y - k[1])
        if dy <= v[1]:
            dx = v[1] - dy
            intervals.append([k[0] - dx, k[0] + dx])
    return mergeIntervals(intervals)

interval, _ = get_intervals(2000000, closest)
m, M = interval[0]
print(abs(M - m + 1) - len(list(sensor for sensor in sensors if sensor[1] == y and m <= sensor[0] <= M)) - len(list(beacon for beacon in beacons if m <= beacon[0] <= M and beacon[1] == y)))

s = Solver()
(x,y) = (Int('x'), Int('y'))
s.add(And([If(zabs(x - k[0]) + zabs(y - k[1]) > v[1], True, False) for k,v in closest.items()]))
s.add(And([x >= 0, x <= 4000000]))
s.add(And([y >= 0, y <= 4000000]))
s.check()
m = s.model()
x, y = m[x].as_long(), m[y].as_long()
print(x * 4000000 + y)
