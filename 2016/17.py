
from collections import deque
from collections import defaultdict
import sys
from hashlib import md5

salt = 'dmypynyp'
path = []
q = deque()
valid = 'bcdef'
lens = []
q.append([[], [0, 0]])
while q:
    x, z = q.popleft()
    if z == [3, 3]:
        lens.append(len(x))
        continue
    a = salt + ''.join(x)
    a = md5(a.encode()).hexdigest()
    a = a[:4]
    if a[0] in valid:
        if not z[0] <= 0:
            newx = [i for i in x]
            newx.append('U')
            q.append([newx, [z[0] - 1, z[1]]])
    if a[1] in valid:
        if not z[0] >= 3:
            newx = [i for i in x]
            newx.append('D')
            q.append([newx, [z[0] + 1, z[1]]])
    if a[2] in valid:
        if not z[1] <= 0:
            newx = [i for i in x]
            newx.append('L')
            q.append([newx, [z[0], z[1] - 1]])
    if a[3] in valid:
        if not z[1] >= 3:
            newx = [i for i in x]
            newx.append('R')
            q.append([newx, [z[0], z[1] + 1]])
print(max(lens))
