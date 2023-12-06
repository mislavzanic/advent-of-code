import re
import itertools as it
from collections import defaultdict

def part1(inlist):
    hi = int(''.join(str(int(x > 500)) for x in [sum(int(l[i]) for l in inlist) for i in range(len(inlist[0]))]), 2)
    lo = int(''.join(str(int(x < 500)) for x in [sum(int(l[i]) for l in inlist) for i in range(len(inlist[0]))]), 2)
    return hi * lo

def get_next(nums, index, hi):
    count = sum(int(l[index]) for l in nums)
    bit = 1 - (count < (len(nums) // 2) + len(nums) % 2) if hi else (count < (len(nums) // 2) + len(nums) % 2)
    return [l for l in nums if int(l[index]) == bit]

def part2(inlist):
    hi, lo = [x for x in inlist], inlist
    for i in range(len(inlist[0])):
        if len(hi) > 1:
            hi = get_next(hi, i, True)
        if len(lo) > 1:
            lo = get_next(lo, i, False)

    return int(hi[0],2) * int(lo[0],2)
