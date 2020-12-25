from collections import defaultdict


d = defaultdict(int)
for x in open('input').readlines():
    x = x.strip().split()
    if x[0] == 'toggle':
        startx, starty = int(x[1][:x[1].find(',')]), int(x[1][x[1].find(',') + 1:])
        endx, endy = int(x[-1][:x[-1].find(',')]), int(x[-1][x[-1].find(',') + 1:])
    else:
        startx, starty = int(x[2][:x[2].find(',')]), int(x[2][x[2].find(',') + 1:])
        endx, endy = int(x[-1][:x[-1].find(',')]), int(x[-1][x[-1].find(',') + 1:])
    for i in range(startx, endx + 1):
        for j in range(starty, endy + 1):
            if x[0] == 'toggle':
                d[(i, j)] += 2
            elif x[1] == 'on':
                d[(i, j)] += 1
            else:
                if d[(i, j)] > 0:
                    d[(i, j)] -= 1

print(sum(d[(i, j)] for i in range(1000) for j in range(1000)))
