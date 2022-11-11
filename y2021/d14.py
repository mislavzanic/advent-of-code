from collections import defaultdict
from typing import Counter

def f(d, n, p):
    p1 = Counter()
    for i in range(0,len(p) - 1): p1[p[i]+p[i+1]] += 1
    for _ in range(n):
        p2 = Counter()
        for k,v in p1.items():
            if k in d.keys():
                p2[k[0]+d[k]] += v
                p2[d[k]+k[1]] += v
        p1 = Counter({k:v for k,v in p2.items()})

    c = Counter()
    for k,v in p1.items():
        c[k[0]] += v

    return max(c.values()) - min(c.values()) + 1 if c[p[-1]] == max(c.values()) else max(c.values()) - min(c.values())

def main(l):
    p = ''
    d = defaultdict(str)
    for line in l:
        line = line.split(" -> ")
        if len(line) < 2:
            if len(line) == 1 and line[0]:
                p = line[0]
            continue
        d[line[0]] = line[1]
    return f(d,10,p), f(d,40,p)
