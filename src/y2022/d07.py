from get_input import get_aoc_input

import itertools as it
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import math



def main():
    l = []
    s = 0
    mem = Counter()
    fs = defaultdict(set)
    visited = []
    with get_aoc_input(7, 2022) as f:
        l = [x.strip() for x in f.readlines()]

    dirs = set()
    for item in l:
        items = item.split(' ')
        if items[0] == '$' and items[1] == 'cd':
            if items[2] == '..':
                visited.pop()
            else:
                visited.append(items[2])

        if items[0] == 'dir':
            fs[tuple(visited)].add(tuple(visited + [items[1]]))
            dirs.add(tuple(visited + [items[1]]))

        if items[0].isnumeric():
            fs[tuple(visited)].add(tuple(visited + [items[1]]))
            mem[tuple(visited + [items[1]])] = int(items[0])


    def rec(currdir, fs, mem):
        s = 0
        for item in fs[currdir]:
            if item in dirs and item not in mem.keys():
                mem[item] = rec(item, fs, mem)
            s += mem[item]
        return s

    rec(('/',), fs, mem)
    for item in fs[('/',)]:
        mem[('/',)] += mem[item]

    s = 0
    for k,v in mem.items():
        if k in dirs and v <= 100000:
            s += v
    print(s)

    total, goal = 70000000, 30000000
    unused = total - mem[('/',)]
    m = []
    for value in mem.values():
        if unused + value >= goal:
            m.append(value)
    print(min(m))



if __name__ == '__main__':
    main()
