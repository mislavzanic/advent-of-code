from collections import defaultdict
from collections import deque

l = [x.strip().split() for x in open('input').readlines()]
d = defaultdict(list)
dd = defaultdict(list)
for x in l:
    if x[4] != 'no':
        i = 0
        while i < len(x) - 6:
            d[x[0] + x[1]].append(x[i+5]+x[i + 6])
            dd[x[0]+x[1]].append({x[i+5]+x[i+6] : int(x[i+4])})
            i += 4

def part1():
    start = deque(['shinygold'])
    num = 0
    seen = ['shinygold']
    while start:
        n = start.popleft()
        for k in d:
            if n in d[k] and k not in seen:
                start.append(k)
                seen.append(k)
                num += 1
    return num

def f(b, seen):
    if b in seen.keys():
        return seen[b]
    if not d[b]:
        seen[b] = 0
        return 0

    for bag in d[b]:
        koef = 0
        for kv in dd[b]:
            if bag in kv.keys():
                koef = kv[bag]
        seen[b] += (f(bag, seen) + 1) * koef
    return seen[b]

seen = defaultdict(int)
print(f('shinygold', seen))
