from collections import defaultdict

infmap = defaultdict(int)
tempmap = []
act = 10000000
for x in open('input').readlines():
    x = x.strip()
    a = [c for c in x]
    tempmap.append(a)

for i in range(len(tempmap)):
    for j in range(len(tempmap[i])):
        infmap[(i, j)] = 0 if tempmap[i][j] == '.' else 2

start = (len(tempmap) // 2, len(tempmap[0]) // 2)
nextdir = {0 : (-1,0), 1 : (0,-1), 2 : (1,0), 3 : (0, 1)}
currdir = 0
num = 0
for i in range(act):
    if infmap[start] == 2:
        currdir = (currdir - 1) % 4
    elif infmap[start] == 0:
        currdir = (currdir + 1) % 4
    elif infmap[start] == 3:
        currdir = (currdir - 2) % 4
    else:
        num += 1
    infmap[start] = (infmap[start] + 1) % 4
    start = (start[0] + nextdir[currdir][0], start[1] + nextdir[currdir][1])
print(num)
