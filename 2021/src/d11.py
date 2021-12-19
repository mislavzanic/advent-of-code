import re
from collections import defaultdict, Counter
import itertools as it

def flash(i,j,l,flashed):
    flashes = 0
    trys = list(it.permutations([-1,0,1],2))+[(1,1),(-1,-1)]
    for x,y in trys:
        if not (-1<x+i<len(l) and -1<y+j<len(l)): continue
        if (x+i,y+j) in flashed: continue
        l[x+i][y+j] = (l[x+i][y+j] + 1) % 10
        if l[x+i][y+j] == 0:
            flashed.add((x+i,y+j))
            flashes += 1 + flash(x+i,y+j,l,flashed)

    return flashes


def main(l):
    for i,item in enumerate(l):
        l[i] = [int(x) for x in item]
    flashes = 0
    for step in range(10000):
        if step == 100:
            print(flashes)
        flashed = set()
        for i,item in enumerate(l):
            for j,num in enumerate(item):
                if (i,j) in flashed: continue
                l[i][j] = (num + 1) % 10
                if l[i][j] == 0:
                    flashed.add((i,j))
                    flashes += 1 + flash(i,j,l,flashed)
        if len(flashed) == 100:
            return step + 1

