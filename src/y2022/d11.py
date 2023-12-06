#!/usr/bin/env python3

from functools import reduce
from get_input import get_aoc_input

import itertools as it
import ast
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import math
import autb


example = False

ll = []

primes = []

class Monkey:
    def __init__(self, items, operator, n, divisible, t, f):
        self.items = items
        self.operator = operator
        self.n = n
        self.divisor = divisible
        self.t = t
        self.f = f
        self.inspected = 0

    def op(self, x):
        if self.n == 'old':
            return x + x if self.operator == '+' else x*x
        return x + int(self.n) if self.operator == '+' else x*int(self.n)

    def test(self, x):
        if x % self.divisor == 0:
            return self.t, x
        return self.f, x

    def do_turn(self):
        throw_to = []
        self.inspected += len(self.items)
        for item in self.items:
            worry = self.op(item)
            worry %= reduce(lambda a,b: a*b, primes)
            # worry = autb.crt([worry for _ in monkeys], [m.divisor for m in monkeys])
            test, worry = self.test(worry)
            throw_to.append((test, worry))
        self.items = []
        return throw_to

if example:
    ll = [x.strip() for x in open('input/11.ex').readlines()]

else:
    with get_aoc_input(11, 2022) as f:
        ll = [x.strip() for x in f.readlines()]

def add(n):
    return
def make_op(n, operator):
    if operator == '+':
        return add(n)

monkeys = []
i = 0
monkey = 0

while i < len(ll):
    item = ll[i]
    while i < len(ll) and ll[i] != '':
        temp = item.split(' ')
        if temp[0] == 'Monkey':
            items = [int(x) for x in ll[i+1].split(': ')[1].split(', ')]
            cond_num = int(ll[i+3].split(': ')[1].split(' ')[-1])
            primes.append(cond_num)
            cond_true = ll[i+4].split(': ')[1].split(' ')[-1]
            cond_false = ll[i+5].split(': ')[1].split(' ')[-1]
            operator = ll[i+2].split(': ')[1].split(' ')[3]
            n = ll[i+2].split(': ')[1].split(' ')[4]
            monkeys.append(Monkey(items, operator, n, cond_num, int(cond_true), int(cond_false)))
            i += 6
        else:
            i += 1
    i += 1


for i in range(10000):
    for m in monkeys:
        throw_to = m.do_turn()
        for item in throw_to:
            monkeys[item[0]].items.append(item[1])


l = sorted([x.inspected for x in monkeys])
print(l)
print(l[-1] * l[-2])
