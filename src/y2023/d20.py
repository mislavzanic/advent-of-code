from functools import reduce
from aoc_util.advent import Input
from collections import defaultdict
import math

'''
303445440 to low
321769440 to low
'''

def run(graph, ff, cnj):
    Q = [('broadcaster', -1, 'button')]
    signals = {-1: 1, 1: 0}
    reached = False
    while Q:
        pos, signal, sendee = Q.pop(0)
        if pos == 'broadcaster':
            for n_pos in graph[pos]:
                signals[signal] += 1
                Q.append((n_pos, signal, pos))
        if pos in ff and signal == -1:
            ff[pos] *= signal
            for n_pos in graph[pos]:
                signals[ff[pos]] += 1
                Q.append((n_pos, ff[pos], pos))
        if pos in cnj:
            cnj[pos][sendee] = signal
            n_signal = -1 if all(v == 1 for v in cnj[pos].values()) else 1
            for n_pos in graph[pos]:
                signals[n_signal] += 1
                Q.append((n_pos, n_signal, pos))
    return signals, reached
    
def parse(day: Input):
    ff, cnj = {}, {}
    graph = {}
    start = 'broadcaster'
    for line in day.lines():
        snd, rcv = line.split(' -> ')
        rcv = rcv.split(', ')
        if snd[0] == '%': ff[snd[1:]] = -1
        if snd[0] == '&': cnj[snd[1:]] = {}
        if snd == start: graph[snd] = rcv
        else: graph[snd[1:]] = rcv
    for k,v in graph.items():
        for mod in v:
            if mod in cnj:
                cnj[mod][k] = -1
    return graph, ff, cnj

def p1(day: Input):
    graph, ff, cnj = parse(day)
    signals = {-1:0, 1:0}
    for _ in range(1000):
        n_signals, _ = run(graph, ff, cnj)
        signals[-1] += n_signals[-1]
        signals[1] += n_signals[1]
    return reduce(lambda x, y: x*y, signals.values())
                
def p2(day: Input):
    graph, ff, cnj = parse(day)
    i = 0
    changes = {}
    states = {}
    for k in graph:
        if k in ff: states[k] = ff[k]
        if k in cnj: states[k] = -1 if all(v == 1 for v in cnj[k].values()) else 1

    i = 0
    l = ['zq', 'qm', 'dc', 'jh']
    while True:
        run(graph, ff, cnj)
        i += 1
        for k in graph:
            if k in ff and states[k] != ff[k]:
                if k in changes: continue
                changes[k] = i
            if k in cnj:
                ns = -1 if all(v == 1 for v in cnj[k].values()) else 1
                if states[k] != ns:
                    if k in changes: continue
                    changes[k] = i
        nl = [k for k in graph if k not in changes and k not in ['ls', 'broadcaster']]
        if sorted(nl) == sorted(l): break

    return reduce(lambda x, y: x*y, [sum(changes[k] for k in cnj[item]) for item in nl])
    
                    
            
                

