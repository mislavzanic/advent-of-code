from collections import defaultdict

def f(i, j, dd, R, C):
    num = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0: continue
            key = (x+i, j+y)
            num += dd[key] == '#'
            if dd[key] == '.':
                k, l = x, y
                while 0 <= k+i < R and 0 <= j+l < C and dd[(k+i, j+l)] == '.':
                    k += x
                    l += y
                key = (i+k, j+l)
                num += dd[key] == '#'
    return num


l = [x.strip() for x in open('input').readlines()]
d = defaultdict(str)
for i,r in enumerate(l):
    for j,c in enumerate(r):
        d[(i, j)] = c
R, C = len(l), len(l[1])
ok = False
p1 = 0
while not ok:
    dd = defaultdict(str)
    ok = True
    for k, v in d.items():
        dd[k] = v
    for i in range(R):
        for j in range(C):
            num = f(i, j, dd, R, C)
            key = (i, j)
            if dd[key] == 'L' and not num:
                d[key] = '#'
                ok = False
            elif dd[key] == '#' and num >= 5:
                d[key] = 'L'
                ok = False
    for c in d.values():
        p1 += c == '#'
    print(p1)
    p1 = 0

