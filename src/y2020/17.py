import re
import fileinput
from collections import defaultdict

l = [x for x in list(fileinput.input())]
p1,p2 = defaultdict(int), defaultdict(int)
for i,line in enumerate(l):
    line = line.strip()
    for j,c in enumerate(line):
        p1[(i-4, j-4, 0)] = 1 if c == '#' else 0
        p2[(i- 4 ,j - 4, 0, 0)]=1 if c == '#' else 0

        
n = 0;

while n < 6:
    dd1, dd2 = defaultdict(int), defaultdict(int)
    for k,v in p1.items():
        dd1[k] = v
    for k,v in p2.items():
        dd2[k] = v
    for i in range(-5-n,6+n):
        for j in range(-5-n,6+n):
            for z in range(-4-n,5+n):
                for w in range(-4-n,5+n):
                    on, off = 0, 0
                    for m in range(-1,2):
                        for l in range(-1,2):
                            for k in range(-1,2):
                                for a in range(-1,2):
                                    if not k == m == l == a == 0:
                                        on += dd[(i+k,j+l,z+m,w+a)]
                                        off += 1 - dd[(i+k,j+l,z+m,w+a)]
                    if (on != 2 and on != 3) and dd[(i,j,z,w)]:
                        d[(i,j,z,w)] = 0
                    elif dd[(i,j,z,w)] == 0 and on == 3:
                        d[(i,j,z,w)] = 1
    n+=1
print(sum(d.values()))
