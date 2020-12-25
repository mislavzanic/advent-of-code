from collections import defaultdict

d = defaultdict(list)

l = [x.strip() for x in open('input').readlines()]
l = l[2:]
for i in range(len(l)):
    x = l[i]
    x = x.split()
    d[i] = [int(x[2][:-1]), int(x[3][:-1])]

p1 = 0
for i in range(len(l)):
    for j in range(len(l)):
        if d[i][0] <= d[j][1] and d[i][0] != 0 and i != j:
            p1 += 1

print(p1)


for x in l:
    if 
