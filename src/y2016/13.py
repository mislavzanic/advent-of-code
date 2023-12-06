from collections import deque 

favnum = 1352
Q = deque([[1, 1, 0]])
been = []
p1, p2 = 0, 0
while Q:
    currpos = Q.popleft()
    if currpos[:2] in been:
        continue

    if currpos[0] == 31 and currpos[1] == 39:
        p1 = length
        print(p1, p2)
    if currpos[2] <= 50:
        p2 += 1

    been.append(currpos[:2])
    x, y, length = currpos
    toexpl = []
    
    for i in range(-1, 2):
        if i != 0:
            if x + i >= 0:
                toexpl.append([x+i, y])
            if y + i >= 0:
                toexpl.append([x, y+i])

    while toexpl:
        x, y = toexpl.pop()
        num = x*x + 3*x + 2*x*y + y + y*y + favnum
        bits = 0
        while num:
            bits += num % 2
            num = num >> 1
        if bits % 2 == 0:
            Q.append([x, y, length + 1])
