import sys
from collections import defaultdict

l = [x.strip() for x in open('input').readlines()]

d = defaultdict(int)
i = 0
d['c'] = 1
while i < len(l):
    x = l[i]
    x = x.split()
    if x[0] == 'cpy':
        if ord(x[1][0]) < 60:
            val = int(x[1])
            d[x[2]] = val
        else:
            d[x[2]] = d[x[1]]
    elif x[0] == 'inc':
        d[x[1]] += 1
    elif x[0] == 'dec':
        d[x[1]] -= 1
    else:
        if ord(x[1][0]) < 60:
            val = int(x[1])
            if val != 0:
                i += int(x[2])
                continue
        else:
            if d[x[1]] != 0:
                i += int(x[2])
                continue
    i += 1
print(d['a'])

        

    
