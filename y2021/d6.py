from collections import defaultdict
import re
import itertools as it

def part1(l):
    d = defaultdict(int)
    for x in l: d[x] = sum(y == x for y in l)
    d[6],d[7],d[8] = 0,0,0
    temp = 0
    for i in range(256):
        if i == 80:
            print(sum(v for v in d.values()))
        temp = d[7]
        d[7] = d[8]
        d[8] = d[i % 7]
        d[i % 7] += temp

    return sum(v for v in d.values())



def main(inlist):
    inlist = inlist[0].split(',')
    inlist = [int(x) for x in inlist]
    return part1(inlist)
