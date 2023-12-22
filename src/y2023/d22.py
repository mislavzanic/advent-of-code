from collections import Counter, defaultdict
from aoc_util.advent import Input
import itertools as it

def parse(day:Input):
    return list(sorted(
        [
            list(map(lambda x: list(map(int, x.split(','))), line.split('~')))
            for line in day.lines()
        ],
        key=lambda x: x[0][2]
    ))

def fall(bricks):
    d = Counter()
    for i, (start, end) in enumerate(bricks):
        z, diff = start[2], 0
        while z-diff-1: 
            x_y_loop = it.product(range(start[0], end[0] + 1), range(start[1], end[1] + 1))
            if any((x,y,z-diff-1) in d for x,y in x_y_loop):
                break
            diff += 1

        for x,y,z in it.product(*list(map(lambda x: range(x[0], x[1] + 1), zip(start, end)))):
            d[x,y,z-diff] = i
    return d

def get_support(d):
    support = defaultdict(set)
    supported = defaultdict(set)
    for (x,y,z),v in d.items():
        if (x,y,z+1) in d and d[x,y,z+1] != v:
            support[v].add(d[x,y,z+1])
            supported[d[x,y,z+1]].add(v)
    return support, supported

def destroyable(d, support):
    destroy = set()
    for k1,v1 in support.items():
        if all(any(x in v2 for k2,v2 in support.items() if k2 != k1) for x in v1):
            destroy.add(k1)
    return destroy | (d.values() - support.keys())

def p2(day: Input):
    bricks = parse(day)
    d = fall(bricks)

    support, supported = get_support(d)
    destroy = destroyable(d, support)

    def bfs(k):
        Q = [({k}, set())]
        while True:
            curr, fall = Q.pop(0)
            if curr == set(): return fall
            next_b = set()
            for b in curr:
                if b not in support: continue
                next_b = next_b | {x for x in support[b] if supported[x] - (curr | fall) == set()}
            Q.append((next_b, fall | next_b))

    return sum(len(bfs(k)) for k in support.keys() - destroy)


def p1(day: Input):
    bricks = parse(day)
    d = fall(bricks)

    support, _ = get_support(d)
    destroy = destroyable(d, support)

    return len(destroy)

        

                    
                
