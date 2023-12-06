from functools import reduce
from collections import defaultdict

def main(day):
    lines = day.lines()
    s = 0
    ok = False
    number = ''
    gear = None
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for j,char in enumerate(line):
            if not char.isnumeric() or j == 0:
                if number != '' and ok:
                    s += int(number)
                    adj[gear].append(int(number))
                number = ''
                ok = False

            if not char.isnumeric(): continue

            number += char
            if ok: continue
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if not (0 <= i + k < len(lines)) or not (0 <= j + l < len(line)):
                        continue
                    if lines[i+k][j+l].isnumeric() or lines[i+k][j+l] == '.':
                        continue
                    gear, ok = (i+k, j+l), True
    print(s)
    s = 0
    for v in adj.values():
        if len(v) == 2:
            s += reduce(lambda x,y: x*y, v)
    print(s)




