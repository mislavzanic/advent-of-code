import fileinput
import re
from collections import defaultdict

lines = [x for x in fileinput.input()]

ingr =  []
contains = []
alg = defaultdict(set)
for line in lines:
    line = line.strip().split()
    cnt = False
    temp = set()
    temp2 = set()
    for string in line:
        if string == '(contains':
            cnt = True
            continue
        if cnt:
            temp2.add(string[:-1])
        else:
            temp.add(string)
    for t in temp2:
        if t in alg.keys():
            a = alg[t].intersection(temp)
            alg[t] = set([c for c in a])
        else:
            for tt in temp:
                alg[t].add(tt)
    ingr.append(temp)
    contains.append(temp2)

                    

num = 0
for i,c in enumerate(ingr):
    for k,v in alg.items():
        ingr[i] = ingr[i].difference(v)
for i,c in enumerate(ingr):
    for cc in c:
        num += 1
print(num)

while True:
    for k,v in alg.items():
        if len(v) == 1:
            for kk,vv in alg.items():
                if k != kk:
                    vv = vv.difference(v)
                    alg[kk] = vv
    ok = True
    for k,v in alg.items():
        if len(v) > 1:
            ok = False
    if ok: break
ing = list()
temp = list()
for k,v in alg.items():
    temp.append(k)
temp.sort()
for a in temp:
    ing.append(list(alg[a])[0])
print(','.join(ing))
