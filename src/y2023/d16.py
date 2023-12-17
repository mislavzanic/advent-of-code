from aoc_util.advent import Input
from collections import Counter

def new_iter(l, positions):
    seen = set() 
    d = Counter()
    while positions:
        p = positions.pop()
        x, y, (dx,dy) = p
        if p in seen: continue
        seen.add(p)


        if not (0 <= x < len(l) and 0 <= y < len(l)): continue
        d[x,y] += 1
        c = l[x][y]
        
        if c == '.':
            positions.append((x + dx, y + dy, (dx, dy)))

        elif c in '/\\':
            ndx, ndy = pow(-1,int(c == '/')) * dy, pow(-1, int(c == '/')) * dx
            positions.append((x + ndx, y + ndy, (ndx, ndy)))

        else:
            if (dx == 0 and c == '-') or (dy == 0 and c == '|'):
                positions.append((x + dx, y + dy, (dx, dy)))
            else:
                positions.append((x + int(c=='|'), y + int(c=='-'), (int(c=='|'),int(c=='-'))))
                positions.append((x - int(c=='|'), y - int(c=='-'), (-int(c=='|'),-int(c=='-'))))
    return d

def p2(day: Input):
    m = []
    for i in range(len(day.lines())):
        for j in range(len(day.lines())):
            if i != 0 and j != 0: continue
            if i in [0,len(day.lines())] and j in [0,len(day.lines())]:
                m.append(len(new_iter(day.lines(), [(i, j, (pow(-1,int(i != 0)) * 1, pow(-1,int(j != 0)) * 0))]).keys()))
                m.append(len(new_iter(day.lines(), [(i, j, (pow(-1,int(i != 0)) * 0, pow(-1,int(j != 0)) * 1))]).keys()))
            else:
                m.append(len(new_iter(day.lines(), [(i, j, (pow(-1,int(i != 0)) * int(i == 0), pow(-1,int(j != 0)) * int(j == 0)))]).keys()))
    return max(m)
    

def p1(day: Input):
    d = new_iter(day.lines(),[(0,0,(0,1))])

    return len(d.keys())
        

