from collections import defaultdict
import re

def part1(coords):
    d = defaultdict(int)
    for x,y,x1,y1 in coords:
        mx, Mx = min(x,x1), max(x,x1)
        my, My = min(y,y1), max(y,y1)
        if mx == Mx or my == My:
            for i in range(mx, Mx + 1):
                for j in range(my, My + 1):
                    d[(i,j)] += 1
    return sum(v > 1 for v in d.values())

def part2(coords):
    d = part1(coords)
    for x,y,x1,y1 in coords:
        mx, Mx = min(x,x1), max(x,x1)
        for i in range(Mx - mx + 1):
            if x < x1:
                if y < y1: d[(x + i, y + i)] += 1
                else: d[(x + i, y - i)] += 1
            else:
                if y < y1: d[(x - i, y + i)] += 1
                else: d[(x - i, y - i)] += 1


def main(inlist):
    d = defaultdict(int)
    coords = []
    for l in inlist:
        m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", l)
        x,y,x1,y1 = int(m.group(1)), int(m.group(2)),int(m.group(3)),int(m.group(4))
        coords.append([x,y,x1,y1])
    return sum(v > 1 for v in d.values())
