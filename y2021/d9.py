from collections import defaultdict
import re
import itertools as it
from functools import reduce

def part2(inlist, low):
    basins = []
    for (xx,yy) in low:
        seen = set()
        Q = [(xx,yy)]
        points = []
        temp = []
        while len(Q) > 0:
            curr = Q.pop(0)
            x,y = curr
            if curr in seen: continue
            seen.add(curr)
            if y < 0 or y > len(inlist) - 1 or x < 0 or x > len(inlist[0]) - 1: continue
            if int(inlist[y][x]) == 9: continue
            if len(points) == 0:
                points.append(int(inlist[y][x]))
                temp.append((y,x))
            else:
                if int(inlist[y][x]) != 9:
                    points.append(int(inlist[y][x]))
            Q+= [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        basins.append(len(points))
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]



def main(inlist):
    s = 0
    low = []
    for j,line in enumerate(inlist):
        for i,l in enumerate(line):
            ok = True
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if x * y == 0 and x != y and -1 < y + j < len(inlist) and -1 < x + i < len(line):
                        ok &= int(inlist[y+j][x+i]) > int(l)
            if ok:
                s += 1+int(l)
                low.append((i,j))
    print(part2(inlist, low))
    return s
