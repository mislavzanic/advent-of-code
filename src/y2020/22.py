import re
import fileinput
from collections import deque

lines = [x.strip() for x in fileinput.input()]
pl = [deque(), deque()]
ind = -1
for line in lines:
    x = line.split()
    if x and x[0] == 'Player':
        ind += 1
        continue
    ints = [int(x) for x in re.findall('-?\d+',line)]
    if ints:
        pl[ind].append(ints[0])

def f(pl):
    winner = None
    s = 0
    config = set()
    while True:
        key = (tuple(pl[0]), tuple(pl[1]))
        if key in config:
            return 0, s
        config.add(key)
        if not pl[0] or not pl[1]:
            if pl[0]:
                winner = 0
                for i in range(len(pl[0])):
                    s += pl[0][i] * (len(pl[0]) - i)
            else:
                winner = 1
                for i in range(len(pl[1])):
                    s += pl[1][i] * (len(pl[1]) - i)
            return winner, s
        p1, p2 = pl[0].popleft(), pl[1].popleft()
        if p1 <= len(pl[0]) and p2 <= len(pl[1]):
            winner, _ = f([deque(list(pl[0])[:p1]), deque(list(pl[1])[:p2])])
            if winner == 0:
                pl[0].append(p1)
                pl[0].append(p2)
            else:
                pl[1].append(p2)
                pl[1].append(p1)
            
        else:
            if p1 > p2:
                pl[0].append(p1)
                pl[0].append(p2)
            if p1 < p2:
                pl[1].append(p2)
                pl[1].append(p1)

print(f(pl))
