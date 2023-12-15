'''
111940 # to low
'''
from aoc_util.advent import Input
from aoc_util import math


def rotate(original, side):
    sides = {'N': 0, 'W':1, 'S':2, 'E':3}
    for _ in range(sides[side]):
        original = math.rotate(original)
    return original

def roll(i,j,l):
    k = i-1
    while len(l) > k > 0 and l[k][j] == '.': k = k - 1
    if k < 0 or l[k][j] != '.': return k+1
    return k

def roll_all(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in '.#': continue
            k = roll(i, j, l)
            if k == i: continue
            l[i][j], l[k][j] = '.', 'O'
    return l

def load(l):
    s = 0
    for i,line in enumerate(l):
        s += sum(int(c == 'O') for c in line) * (len(l) - i)
    return s

def p2(day: Input):
    s = []
    l = [[c for c in line] for line in day.lines()]
    N = 1000000000
    period,idx = -1, -1
    repeats = []
    while True:
        cycle = []
        for side in 'NWSE':
            l = rotate(roll_all(rotate(l, side)), 'NWSE'[(4 - 'NWSE'.index(side)) % 4])
            cycle.append(load(l))
        if cycle in s:
            idx = s.index(cycle)
            period = len(s) - idx
            # if len(repeats) > 0 and idx != repeats[-1] + 1:
                # print(idx, repeats[-1], repeats)
                # print(cycle, period, idx, (N-idx) % period, len(s), s[idx - 1 + ((N - idx) % period)][-1])
                # repeats = []
            repeats.append(idx)
            print(repeats[-1], cycle, s[idx], len(s))
            # if len(repeats) >= period: break
            # print(cycle, period, idx, (N-idx) % period, len(s), s[idx - 1 + ((N - idx) % period)][-1])
            # break
        s.append(cycle)
    return s[idx - 1 + ((N - idx) % period)][-1]

def p1(day: Input):
    return load(roll_all([[c for c in line] for line in day.lines()]))
