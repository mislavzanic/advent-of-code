from collections import defaultdict
import sys

dists = defaultdict(int)

pos = []
i = 0
for x in open('input').readlines():
    x = x.strip()
    p = x[x.find('p') + 3: x.find('>', x.find('p'))]
    y = p.split(',')
    z = []
    for n in y:
        z.append(int(n))
    v = x[x.find('v') + 3: x.find('>', x.find('v'))]
    y = v.split(',')
    for n in y:
        z.append(int(n))
    a = x[x.find('a') + 3: x.find('>', x.find('a'))]
    y = a.split(',')
    for n in y:
        z.append(int(n))
    pos.append(z)
    i += 1

it = 0
while it < 1000:
    it += 1
    col = defaultdict(list)
    for p in pos:
        p[0] += it*p[6] + p[3]
        p[1] += it*p[7] + p[4]
        p[2] += it*p[8] + p[5]
        col[(p[0], p[1], p[2])].append(p)
    for k, v in col.items():
        if len(v) > 1:
            for i in v:
                pos.remove(i)
print(len(pos))

for i, x in enumerate(pos):
    dists[i] = abs(x[0]) + abs(x[1]) + abs(x[2])
maxi = 0
maxd = -1
for k,v in dists.items():
    if maxd < 0 or v < maxd:
        maxd = v
        maxi = k
print(maxi)
