import itertools as it
import re
from collections import defaultdict, Counter


def main(l):
    img = l[0]
    l = l[2:]
    c = defaultdict(lambda:'.')
    m = len(l)
    for i,line in enumerate(l):
        for j,char in enumerate(line):
            c[(i,j)] = char

    t = 0
    while t < 2:
        if t == 2:
            print(sum(v == '#' for v in c.values()))
        d = img[0] if t % 2 else '.'
        nc = defaultdict(lambda:'.' if t % 2 else img[0])

        for i in range(-m,m+2):
            for j in range(-m,m+2):
                c[(i,j)] = c[(i,j)]

        for i,j in c.keys():
            s = ''
            for k in [-1,0,1]:
                s = s + ''.join(d if (i+k,j+l) not in c.keys() else c[(i+k,j+l)] for l in [-1,0,1])

            s = s.replace('.','0').replace('#','1')
            nc[(i,j)] = img[int(s,2)]
        c = defaultdict(lambda:d)
        for k,v in nc.items(): c[k] = v
        t += 1
        m += 2

    return sum(v == '#' for v in c.values())
