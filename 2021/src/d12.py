import itertools as it
import re
from collections import defaultdict, Counter

def part1(curr, l):
    return curr == curr.lower() and curr in l

def part2(curr, l):
    if curr in ['start','end'] and curr in l: return True
    if curr in l and curr.lower() == curr:
        c = Counter(l)
        return any(k == k.lower() and c[k] == 2 for k in c.keys())

def pathfinding(d, part):
    Q = [('start',[])]
    paths = []
    while len(Q) > 0:
        curr,l = Q.pop()
        if part(curr,l): continue
        l.append(curr)
        if curr == 'end':
            paths.append(l)
            continue
        if curr in d.keys():
            for v in d[curr]:
                Q.append((v,[x for x in l]))
        for k,v in d.items():
            if curr in v:
                Q.append((k,[x for x in l]))

    return len(paths)

def main(l):
    d = defaultdict(list)
    for line in l:
        line = line.split('-')
        d[line[0]] += [line[1]]
    return pathfinding(d, part1), pathfinding(d,part2)
