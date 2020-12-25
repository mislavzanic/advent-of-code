from collections import defaultdict
from collections import deque

d = defaultdict(int)
W = 50
H = 6
for x in open('input').readlines():
    x = x.strip().split()
    if x[0] == 'rect':
        width = int(x[1][:x[1].find('x')])
        height = int(x[1][x[1].find('x') + 1:])
        for i in range(height):
            for j in range(width):
                d[tuple((i, j))] = 1
    else:
        if x[1] == 'row':
            row = int(x[2][x[2].find('=') + 1:])
            offset = int(x[4])
            q = deque()
            for i in range(W):
                q.append(d[tuple((row, i))])
            q.rotate(offset)
            for i in range(W):
                d[tuple((row, i))] = q.popleft()
        else:
            column = int(x[2][x[2].find('=') + 1:])
            offset = int(x[4])
            q = deque()
            for i in range(H):
                q.append(d[tuple((i, column))])
            q.rotate(offset)
            for i in range(H):
                d[tuple((i, column))] = q.popleft()
num = 0
picture = [[' ' for _ in range(50)] for _ in range(6)]
for x in d.values():
    num += x
for x in d.items():
    i, j = x[0]
    picture[i][j] = '#' if x[1] == 1 else ' '
print(num)
print('')
for i in range(6):
        print(''.join(picture[i]))
