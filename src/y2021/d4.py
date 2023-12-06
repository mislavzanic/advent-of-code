import itertools as it
from collections import defaultdict
import re

def won(board, nums):
    if len(nums) < 5: return False
    if len(board) < 5: return False
    return any(all(y in nums for y in x) for x in board) or any(all(board[i][j] in nums for i in range(len(board))) for j in range(len(board[0])))

def part1(inlist):
    numbers = [int(x) for x in inlist[0].split(',')]
    d,j,temp = defaultdict(list),0,[]
    for i,l in enumerate(inlist):
        if not i: continue
        if len(l):
            temp.append([int(x) for x in l.split()])
        else:
            d[j] = [x for x in temp]
            j += 1
            temp = []

    d[j] = [x for x in temp]
    bw = set()
    for i in range(len(numbers)):
        for k in range(j+1):
            if won(d[k], numbers[:i+1]):
                if not len(bw):
                    print(numbers[i] * sum(sum(y for y in x if y not in numbers[:i+1]) for x in d[k]))
                bw.add(k)
                if len(bw) == len(d.keys()) - 1:
                    return numbers[i] * sum(sum(y for y in x if y not in numbers[:i+1]) for x in d[k])
