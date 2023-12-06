from collections import defaultdict

d = defaultdict(int)
k = 1
l = 0
num = 1
for i in range(-2, 3):
    for j in range(-l, l+1):
        d[(i,j)] = k
        k += 1
    l += num
    if l == 2:
        num = -1

pos = (0, -2)
num = []
for x in open('input').readlines():
    x = x.strip()
    pos = list(pos)
    for c in x:
        if c == 'U':
            if pos[0] - abs(pos[1]) > -2:
                pos[0] -= 1
        elif c == 'D':
            if pos[0] + abs(pos[1]) < 2:
                pos[0] += 1
        elif c == 'L':
            if pos[1] - abs(pos[0]) > -2:
                pos[1] -= 1
        else:
            if pos[1] + abs(pos[0]) < 2:
                pos[1] += 1
    pos = tuple(pos)
    num.append(d[pos])
print(num)
