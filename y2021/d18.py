import itertools as it
import re
from collections import defaultdict, Counter
import ast
from typing import Any, List, Tuple, Union
import sys

def explode(to_explode: List[Any], snum: List[Any], whole: List[Any], stack, branch: int):

    def add_num(num, snum, i):
        if type(snum[i]) == list:
            add_num(num,snum[i], i)
        else:
            snum[i] += num

    def find(curr,stack,found):
        if found != None: return found
        if curr == to_explode: return stack
        if type(curr) == int: return
        found = find(curr[0], stack + [0],found)
        if found == None: return find(curr[1], stack + [1],found)
        else: return found

    def propagate(num, whole, m, stack, i):
        if m == -1: return
        if m > 0:
            j = stack.pop(0)
            propagate(num, whole[j], m - 1,stack, i)
        else:
            if type(whole[i]) == list: add_num(num, whole[i], 1-i)
            else: whole[i] += num

    i = snum.index(to_explode)
    m = max([-1] + [j for j in range(len(stack)) if stack[j] != i])

    propagate(to_explode[i], whole, m,stack, i)

    snum[i] = 0
    if type(snum[1-i]) == list: add_num(to_explode[1-i], snum[1-i], i)
    else: snum[1-i] += to_explode[1-i]


def sreduce(snum):
    def check_explode(snum, whole, stack):
        for i,item in enumerate(snum):
            if type(item) == list:
                if len(stack) >= 3:
                    explode(snum[i], snum, whole, stack, i)
                    return 1
                else:
                    t = check_explode(snum[i], whole, stack + [i])
                    if t == 1: return t
        return 0

    def split(snum, whole, stack):
        for i,item in enumerate(snum):
            if type(item) == int:
                if item >= 10:
                    snum[i] = [item // 2, item - (item // 2)]
                    return 2
            else:
                t = split(snum[i], whole, stack + [i])
                if t == 2: return t
        return 0

    t = 0
    if check_explode(snum, snum, []): return 1
    return split(snum, snum, [])


def add(l, snum):
    l = [l,snum]
    while True:
        t = sreduce(l)
        if t == 0: break
    return l

def magnitude(node):
    if type(node) == int: return node
    return 3*magnitude(node[0]) + 2*magnitude(node[1])

def parse(l):
    output = []
    for line in l:
        num = ast.literal_eval(line)
        output.append(num)
    return output

def main(inlist):
    l = parse(inlist)
    arr = []
    ll = parse(inlist)
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                arr.append(magnitude(add(l[i],l[j])))
                l = parse(inlist)
    while len(ll) > 1:
        snum = ll.pop(0)
        ll[0] = add(snum,ll[0])

    return magnitude(ll[0]), max(arr)
