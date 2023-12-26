from aoc_util.advent import Input
import itertools as it
from collections import defaultdict
import sys
import heapq

def parse(day: Input, p2=False):
    d = {}
    for i,line in enumerate(day.lines()):
        for j,char in enumerate(line):
            if p2 and char in '<>^v':
                d[i,j] = '.'
            else: d[i,j] = char
    return (0,1), (len(day.lines()) - 1, len(day.lines()[0]) - 2), d
        
def build_dag(start, end, d):
    Q = [(start, [])]
    graph = defaultdict(set)
    lengths = defaultdict(set)
    slope = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}
    while Q:
        curr, path = Q.pop(0)
        if curr in path: assert False
        path.append(curr)
        if curr == end:
            graph[path[0]].add(end)
            lengths[(path[0], end)].add(len(path) - 1)
            continue

        if curr in graph[path[0]]: continue

        x,y = curr
        if d[x,y] in '<>v^':
            i,j = slope[d[x,y]]
            if (x+i,y+j) in path: assert False, path
            Q.append(((x+i,y+j), path))
            continue

        neigh = []
        for i,j in it.product([-1,0,1], [-1,0,1]):
            if abs(i) + abs(j) != 1: continue
            if (x+i,y+j) not in d: continue
            if d[x+i,y+j] == '#': continue
            if (x+i,y+j) in path: continue
            neigh.append((x+i,y+j))

        if len(neigh) > 1:
            graph[path[0]].add(curr)
            if (path[0], curr) in lengths: assert False
            lengths[(path[0], curr)].add(len(path) - 1)
            # print(len(path), path[0], curr, path)
            path = [curr]

        for n in neigh:
            if d[n] in slope.keys():
                if (slope[d[n]][0] + n[0], slope[d[n]][1] + n[1]) == curr: continue
            Q.append((n, [x for x in path]))

    return graph, lengths

def p2(day: Input):
    start, end, d = parse(day, p2=True)
    graph, lengths = build_dag(start, end, d)

    def dp(start, end, to_visit, DP):
        if (start,end) in lengths: return max(lengths[start,end])
        if (start,end,tuple(to_visit)) in DP: return DP[start,end,tuple(to_visit)]

        val = 0
        for nn in graph[start]:
            if nn not in to_visit: continue
            val = max(val, max(lengths[start, nn]) + dp(nn, end, to_visit - {nn}, DP))
        DP[start,end,tuple((to_visit))] = val
        return val

    return dp(start, end, graph.keys() - {start, end}, {}) 

def topo_sort(start, dag):
    L = []
    S = {start}

    while S:
        node = S.pop()
        L.append(node)
        connected = {x for x in dag[node]}
        for m in connected:
            dag[node].remove(m)
            if all(m not in v for v in dag.values()):
                S.add(m)
    return L
            
def p1(day: Input):
    start, end, d = parse(day)
    dag, lengths = build_dag(start, end, d)

    L = topo_sort(start, dag)
    dist = defaultdict(int)

    if not all(v == set() for v in dag.values()): assert False, "not dag"

    for i,n in enumerate(L):
        for j,m in enumerate(L):
            if i >= j: continue
            if (n,m) not in lengths: continue
            if dist[m] < dist[n] + max(lengths[n,m]):
                dist[m] = dist[n] + max(lengths[n,m])
    return dist[end]
        


            

    

    # return bfs(*parse(day))
# 1319 to low
# 2099 to low
    
