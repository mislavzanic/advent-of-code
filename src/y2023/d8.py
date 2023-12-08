from aoc_util.advent import Input
from collections import defaultdict
import math
import re


def parse(day: Input):
    d = defaultdict(list)
    path, graph = day.string().split("\n\n")
    for line in graph.split("\n"):
        g = re.search(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line).groups()
        d[g[0]] = [g[1], g[2]]
    return path, d

def find_end(start, ends, path, graph):
    i, Q = 0, [start]
    while True:
        curr = Q.pop()
        if curr in ends: break
        Q.append(graph[curr][1 if path[i % len(path)] == 'R' else 0])
        i += 1
    return i

def p1(day: Input):
    return find_end('AAA', ['ZZZ'], *parse(day))

def p2(day: Input):
    path, graph = parse(day)
    start = [x for x in graph.keys() if x[-1] == 'A']
    end = [x for x in graph.keys() if x[-1] == 'Z']
    loops = [find_end(x, end, path, graph) for x in start]
    return math.lcm(*loops)
        

    



