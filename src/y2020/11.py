import fileinput
import re

def findSeats(x, y, d, part2, R, C):
    num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            if 0 <= x+i < R and 0 <= y+j < C:
                num += d[x+i][y+j] == '#'
                if part2 and d[x+i][j+y] == '.':
                    k, l = i, j
                    while 0 <= k+x < R and 0 <= l+y < C and d[k+x][l+y] == '.':
                        k += i
                        l += j
                    if 0 <= k+x < R and 0 <= l+y < C:
                        num += d[x+k][y+l] == '#'
    return num


p1, p2 = 0, 0
l = [x for x in list(fileinput.input())]
d = [list(s) for s in l]

ok = False
while not ok:
    i, j = 0, 0
    ok = True
    dd = [[cr for cr in r] for r in d]
    for i,r in enumerate(dd):
        for j,c in enumerate(r):
            P2 = findSeats(i, j, dd, True, len(l), len(l[0]))
            #P1 = findSeats(i, j, dd, False, len(l), len(l[0]))
            if dd[i][j] == 'L' and not P2:
                d[i][j] = '#'
                ok = False
            elif dd[i][j] == '#' and P2 >= 5:
                d[i][j] = 'L'
                ok = False
    for r in d:
        for v in r:
            p1 += v == '#'
    print(p1)
    p1 = 0

