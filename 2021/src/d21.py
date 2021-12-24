import itertools as it
import re
from collections import defaultdict, Counter


def part1(position):
    points = Counter()
    count = 0
    die = 1
    player = 0
    while True:
        if any(x >= 1000 for x in points.values()):
            p = points[0] if points[0] < 1000 else points[1]
            return p * count

        offset = sum(x % 100 or 100 for x in range(die,die+3))
        die = (die + 3) % 100 or 100

        p = (position[player] + offset) % 10 or 10
        position[player] = p
        points[player] += p

        count += 3
        player = 1 - player

def next_set(p1,p2,i,wins):
    c = Counter()
    throws,outcome = [i+3 for i in range(0,7)],[1,3,6,7,6,3,1]
    for k,v in p1.items():
        if k[0] >= 21: continue
        for (t,o) in zip(throws,outcome):
            key = (k[1] + t) % 10 or 10
            c[(key + k[0],key)] += o * v

    wins[i % 2] += sum(v for k,v in c.items() if k[0] >= 21) * sum(v for k,v in p2.items() if k[0] < 21)
    return c

def iterate(pos1,pos2):
    p1 = Counter()
    p2 = Counter()
    p1[(0,pos1)] = 1
    p2[(0,pos2)] = 1
    wins = [0,0]
    i = 0

    while any(x[0] < 21 for x in p1.keys()) or any(x[0] < 21 for x in p2.keys()):
        p1 = next_set(p1,p2,i,wins)
        p2 = next_set(p2,p1,i+1,wins)
        i += 2
    return max(wins)

def part2(position):
    return iterate(position[0],position[1])

def main(l):
    position = Counter()
    position[0] = 4
    position[1] = 3
    p1 = part1(position)
    position[0] = 4
    position[1] = 3
    return p1,part2(position)
