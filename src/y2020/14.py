import re
import fileinput
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


def findAll(mask, num):
    addr = set()
    pows = []
    for i,c in enumerate(mask):
        if c == 'X':
            pows.append(1 << len(mask) - 1 - i)
    sets = list(powerset(pows))
    mask1 = int(''.join([c if c != 'X' else '0' for c in mask]), base=2)
    aux = int(''.join(['1' if c != 'X' else '0' for c in mask]), base=2)
    for c in sets:
        addr.add(((num & aux) | (sum(c) | mask1)))
    return addr


lines = [x for x in list(fileinput.input())]
p1,p2 = {},{}
mask = 0

for line in lines:
    words = line.strip().split()
    addr = set()
    if words[0] == 'mask':
        mask = [c for c in words[2]]
    else:
        ints = [int(x) for x in re.findall('-?\d+',line)]
        mask1 = int(''.join([c if c != 'X' else '1' for c in mask]),base=2)
        mask2 = int(''.join([c if c != 'X' else '0' for c in mask]),base=2)
        p1[ints[0]] = (ints[1] | mask2) & mask1
        addr = findAll(mask, ints[0])
        for m in addr:
            p2[m] = ints[1]
print(sum(p1.values()))
print(sum(p2.values()))
