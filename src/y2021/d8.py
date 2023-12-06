#!/usr/bin/env python3

import itertools as it
import re
from collections import defaultdict

def part2(nums):
    nums.sort(lambda x: len(x))
    d = defaultdict(str)
    d['a'] = list(set(nums[1]) - set(nums[0]))[0]
    d['g'] = list((set(nums[-2]) & set(nums[-3])) - (set(nums[2]) | set(nums[1])))[0]
    d['e'] = list(set(nums[-1]) - set(set(nums[2]) | set(nums[1]) | set(d['g'])))[0]
    for num in nums:
        num = list(x for x in num)
        if len(set(num) - (set(nums[1]) | set(d['g']))) == 1:
            d['d'] = list(set(num) - (set(nums[1]) | set(d['g'])))[0]
            d['b'] = list(set(nums[2]) - set(nums[0]) - set(d['d']))[0]
    for num in nums:
        num = list(x for x in num)
        if len(set(num) - set([d['a'], d['b'], d['d'], d['g']])) == 1:
            d['f'] = list(set(num) - set([d['a'], d['b'], d['d'], d['g']]))[0]
            d['c'] = list(set(nums[0])- set(d['f']))[0]
    temp = defaultdict(list)
    temp[list(d['c']+d['f']).sort()] = 1
    temp[list(d['a']+d['c']+d['d']+d['e']+d['g']).sort()] = 2
    temp[list(d['a']+d['c']+d['d']+d['f']+d['g']).sort()] = 3
    temp[list(d['a']+d['b']+d['d']+d['f']+d['g']).sort()] = 5
    temp[list(d['b']+d['c']+d['d']+d['f']).sort()] = 4
    temp[list(d['a']+d['c']+d['f']).sort()] = 7
    temp[list(d['a']+d['b']+d['c']+d['d']+d['e']+d['f']+d['g']).sort()] = 8
    temp[list(d['a']+d['b']+d['c']+d['e']+d['f']+d['g']).sort()] = 0
    temp[list(d['a']+d['b']+d['d']+d['e']+d['f']+d['g']).sort()] = 6
    temp[list(d['a']+d['b']+d['c']+d['d']+d['f']+d['g']).sort()] = 9
    return temp


def part1(inlist):
    d = defaultdict(str)
    ss = 0
    for l in inlist:
        l = l.split(' | ')
        dd = part2(l[0].split())
        nums = l[1].split()
        s = 0
        for num in nums:
            s = 10 * s + dd[list(num).sort()]
        ss += s



                #d[num[0] + num[2] + num[5]] = 7
                #d[num[2] + num[5]] = 1
                #d[num[1] + num[2] + num[3] + num[5]] = 4
    print(ss)



def main(inlist):
    return part1(inlist)
