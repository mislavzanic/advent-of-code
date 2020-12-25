from collections import defaultdict


l = [x.strip() for x in open('input').readlines()]
p1 = ''
p2 = ''
for i in range(len(l[0])):
    d = defaultdict(int)
    for j in range(len(l)):
        d[l[j][i]] += 1
    sorted_d = sorted(d.items(), key=lambda kv:kv[1])
    p1 += sorted_d[-1][0]
    p2 += sorted_d[0][0]
print(p1, p2)
