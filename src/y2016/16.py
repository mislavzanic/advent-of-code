from collections import defaultdict
from collections import deque
import sys



x = '10111011111001111'

while len(x) < 35651584:
    y = [c for c in x]
    for i in range(len(y)):
        y[i] = '1' if y[i] == '0' else '0'
    y = ''.join(y)
    y = ''.join([y[i] for i in range(len(y) - 1, -1, -1)])
    assert len(y) == len(x)
    x += '0' + y

x= x[:35651584]
goal = []
while len(x) % 2 == 0:
    newx = []
    for i in range(0, len(x), 2):
        c = '1' if x[i] == x[i + 1] else '0'
        newx.append(c)
    x = newx

print(''.join(x))


