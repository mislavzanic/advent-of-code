from collections import Counter
from queue import PriorityQueue
from functools import reduce
import math
import sys
from z3 import *

def parse(l: list[str]) -> list[tuple[int]]:
    import re

    bots = []
    for item in l:
        bots.append(tuple(map(int, re.findall(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', item)[0])))
    return bots

def md(b1, b2):
    if len(b1) == 4:
        b1 = b1[:-1]
    if len(b2) == 4:
        b2 = b2[:-1]
    return sum(map(lambda c: abs(c[0] - c[1]), zip(b1,b2)))

def get_all_cubes(p1, p2):
    x, y, z = p1
    X, Y, Z = p2
    mx, my, mz = (x + X) // 2, (y + Y) // 2, (z + Z) // 2
    return [
        ((x, y, z), (mx, my, mz)),
        ((mx+1, my+1, mz+1), (X, Y, Z)),
        ((mx+1, y, z),(X, my, mz)),
        ((x, my+1, z),(mx, Y, mz)),
        ((x, y, mz+1),(mx, my, Z)),
        ((mx+1, my+1, z),(X, Y, mz)),
        ((mx+1, y, mz+1),(X, my, Z)),
        ((x, my+1, mz+1),(mx, Y, Z)),
    ]

def bot_in_cube(p1, p2, bot):
    return p1[0] <= bot[0] <= p2[0] and p1[1] <= bot[1] <= p2[1] and p1[2] <= bot[2] <= p2[2]

def bots_in_cube(p1, p2, bots):
    return sum(1 for x in bots if bot_in_cube(p1, p2, x))

def get_cube_corners(cube):
    p1, p2 = cube
    x,y,z = p1
    X,Y,Z = p2

    return [
        (x,y,z), (X,y,z), (x,Y,z), (x,y,Z),
        (X,Y,z), (x,Y,Z), (X,y,Z), (X,Y,Z),
        ((X - x) // 2, (Y - y) // 2, (Z - z) // 2)
    ]

def intersects(bot, cube):
    points = get_cube_corners(cube)
    r = bot[-1]
    bot = bot[:-1]
    return any(1 for p in points if md(p, bot) <= r)

def part2(p1, p2, bots, d, counter):
    cubes = get_all_cubes(p1,p2)
    if md(p1, p2) <= d:
        s = [sum(1 for x in bots if md(x, p) <= x[-1]) for p in get_cube_corners((p1,p2))]
        counter[(p1,p2)] = max(s)
        return
    for cube in cubes:
        part2(cube[0], cube[1], bots, d, counter)


def main():
    l = [x.strip() for x in open('input').readlines()]
    bots = parse(l)
    b = max(bots, key=lambda b: b[-1])
    # print(sum(1 for x in bots if md(x, b) <= b[-1]))

    def zabs(x):
        return If(x >= 0,x,-x)

    (x,y,z) = (Int('x'),Int('y'),Int('z'))
    in_ranges = [Int(f'in_range_{i}') for i in range(len(bots))]
    num_of_bots = Int('sum')
    dist_from_zero = Int('dist')

    o = Optimize()
    for i, bot in enumerate(bots):
        nx, ny, nz, nr = bot
        o.add(in_ranges[i] == If(zabs(x-nx) + zabs(y-ny) + zabs(z-nz) <= nr, 1, 0))
    o.add(num_of_bots == sum(in_ranges))
    o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
    h1 = o.maximize(num_of_bots)
    h2 = o.minimize(dist_from_zero)
    o.check()
    print(o.model().model)
    for item in o.model():
        print(item)



#     X, Y, Z = max(bots, key=lambda b: b[0])[0], max(bots, key=lambda b: b[1])[1], max(bots, key=lambda b: b[2])[2]
#     x, y, z = min(bots, key=lambda b: b[0])[0], min(bots, key=lambda b: b[1])[1], min(bots, key=lambda b: b[2])[2]

#     c = Counter()
#     part2((x,y,z), (X,Y,Z), bots, 2 * min(bots, key=lambda b: b[-1])[-1], c)

#     m = max(c.items(), key=lambda kv: kv[1])[0]
#     print(m)
#     mx,my,mz = max(get_cube_corners(m), key=lambda p: sum(1 for b in bots if md(b,p) <= b[-1]))
#     for p1 in get_cube_corners(m):
#         for p2 in get_cube_corners(m):
#             if p1 == p2: continue
#             if len([x[0] - x[1] for x in zip(p1,p2) if x[0] != x[1]]) != 1: continue



#     # print(md((0,0,0), p[0]), md((0,0,0), p[1]))
#     # print(reduce(lambda x, y: x * y, map(lambda c: abs(c[0] - c[1]), zip(p[0],p[1]))))

if __name__ == '__main__':
    main()
