import itertools as it
import re
from collections import defaultdict
from typing import List,Dict,Tuple,Iterable

COST = {'A':1,'B':10,'C':100,'D':1000}
COORDS = {'A':(0,2),'B':(0,4),'C':(0,6),'D':(0,8)}
N = 2
DP = {}
START = {
    'A' : ['D','D'],
    'B' : ['C','A'],
    'C' : ['B','C'],
    'D' : ['B','A']
 }
END = {
    'A' : ['A','A'],
    'B' : ['B','B'],
    'C' : ['C','C'],
    'D' : ['D','D']
}

def manh_d(x,y):
    return sum(abs(a-b) for (a,b) in zip(x,y))


def deserialize(state) -> Tuple[Dict[str, List[str]], Dict[Tuple[int,int], str]]:
    return ({x[0]:list(x[1]) for x in state[0]},{x[0]:x[1] for x in state[1]})


def serialize(pos,aux) -> Tuple[Tuple,Tuple]:
    return (tuple(list((k,tuple(v)) for k,v in pos.items())),tuple(list((k,v) for k,v in aux.items())))


def from_aux_to_pos(pos,aux):
    for k,v in aux.items():
        if v in pos.keys():
            A = pos[v]
            if len(A) == 0 or (len(A) < N and all(x == v for x in A)):
                c1,c2 = COORDS[v],k
                s = set([(0,i) for i in range(min(c2[1],c1[1])+1,max(c2[1],c1[1]))]) & aux.keys()
                if any(aux[x] != '' for x in s):
                    continue
                pos[v].append(v)
                aux[k] = ''
                yield serialize(pos,aux), (manh_d(k,COORDS[v]) + (N + 1 - len(A))) * COST[v]
                aux[k] = v
                pos[v].pop()


def from_pos_to_aux(pos,aux):
    for k,v in pos.items():
        if len(v) == 0: continue
        if all(x == k for x in v): continue
        char = v.pop()
        candidate = []
        start = [(COORDS[k][0],COORDS[k][1] + 1), (COORDS[k][0],COORDS[k][1] - 1)]
        seen = set()

        while len(start) > 0:
            curr = start.pop()
            if curr in seen: continue
            seen.add(curr)
            if curr in aux.keys() and aux[curr] == '':
                candidate.append(curr)
                start += [(curr[0],curr[1] + 2),(curr[0],curr[1] - 2),(curr[0],curr[1] + 1),(curr[0],curr[1]-1)]

        for c in candidate:
            assert c in aux.keys(), c
            aux[c] = char
            yield serialize(pos,aux), (manh_d(COORDS[k],c) + N - len(v)) * COST[char]
            aux[c] = ''

        v.append(char)


def nextmoves(pos:Dict[str,List],aux:Dict[Tuple,str]) -> Iterable[Tuple[Tuple[Tuple,Tuple],int]]:
    for s,c in from_aux_to_pos(pos,aux):
        yield s,c
    for s,c in from_pos_to_aux(pos,aux):
        yield s,c


def cost(state,i,end):
    pos,aux = deserialize(state)
    assert state in DP.keys(),state
    #c = DP[state]
    nm = [(ns,nc) for ns,nc in nextmoves(pos,aux)]
    for ns,nc in nm:
        if ns not in DP.keys() or DP[ns] > DP[state] + nc:
            DP[ns] = DP[state] + nc
            cost(ns, i+1,end)
        if ns == serialize(end,{x:'' for x in [(0,j) for j in [0,1,3,5,7,9,10]]}): continue


def get_start(part1=False):
    global N
    start = {k:[x for x in v] for k,v in START.items()}
    end = {k:[x for x in v] for k,v in END.items()}
    if part1: return start,end
    start['A'] = start['A'][:1] + ['D','D'] + start['A'][1:]
    start['B'] = start['B'][:1] + ['B','C'] + start['B'][1:]
    start['C'] = start['C'][:1] + ['A','B'] + start['C'][1:]
    start['D'] = start['D'][:1] + ['C','A'] + start['D'][1:]
    end['A'] = end['A'][:1] + ['A','A'] + end['A'][1:]
    end['B'] = end['B'][:1] + ['B','B'] + end['B'][1:]
    end['C'] = end['C'][:1] + ['C','C'] + end['C'][1:]
    end['D'] = end['D'][:1] + ['D','D'] + end['D'][1:]
    N = 4
    return start,end

def main(l):
    global DP
    rest = [(0,i) for i in [0,1,3,5,7,9,10]]
    aux = {x:'' for x in rest}
    start,end = get_start(True)
    DP[serialize(start,aux)] = 0
    cost(serialize(start,aux),0,end)
    p1 = DP[serialize(end,{x:'' for x in rest})]
    start,end = get_start()
    DP = {serialize(start,aux):0}
    start,end = get_start()
    cost(serialize(start,aux),0,end)
    return p1,DP[serialize(end,{x:'' for x in rest})]
