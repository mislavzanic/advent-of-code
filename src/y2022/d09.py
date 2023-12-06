#!/usr/bin/env python3

from get_input import get_aoc_input
from collections import Counter, defaultdict, deque


def touch(x, y) -> bool:
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1

def simulate(hc, tc):
    if not touch(hc, tc):
        dirs = [(-1,0), (1,0), (0,1), (0,-1)] if (hc[0] - tc[0]) * (hc[1] - tc[1]) == 0 else [(-1,-1), (1,1), (-1,1), (1,-1)]
        for xy in dirs:
            if touch(hc, (tc[0] + xy[0], tc[1] + xy[1])):
                return (tc[0] + xy[0], tc[1] + xy[1])
        assert(False)
    return tc

def main(example):
    l = []

    if example == '':
        with get_aoc_input(9, 2022) as f:
            l = [x.strip() for x in f.readlines()]
    else:
        l = [x.strip() for x in open(example).readlines()]

    directions = {'U': (-1, 0), 'D': (1,0), 'L':(0, -1), 'R':(0, 1)}
    p1, p2 = Counter(), Counter()
    rope = [(0,0) for _ in range(10)]

    for item in l:
        curr_dir, much = item.split(' ')
        much = int(much)
        while much:
            x, y = rope[0]
            rope[0] = (x + directions[curr_dir][0], y + directions[curr_dir][1])
            for i in range(len(rope) - 1):
                t = simulate(rope[i], rope[i+1])
                rope[i+1] = t
            p1[rope[1]] += 1
            p2[rope[-1]] += 1
            much -= 1


    print(len(p1.keys()), len(p2.keys()))



if __name__ == '__main__':
    main('')
    # main('input/9.ex')
