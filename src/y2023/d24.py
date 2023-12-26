import enum
from aoc_util.advent import Input
from collections import Counter, defaultdict
import itertools as it
import numpy as np


def parse(day: Input):
    dots = [
        list(map(lambda x: list(map(int, x.split(', '))), line.split(' @ ')))
        for line in day.lines()
    ]
    return dots

def p2(day: Input):
    import z3

    dots = parse(day)

    x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')
    dx, dy, dz = z3.Int('dx'), z3.Int('dy'), z3.Int('dz')

    times = [z3.Int(f'time_{i}') for i in range(len(dots))]

    s = z3.Solver()

    for i, (pos, vel) in enumerate(dots):
        s.add(x + dx * times[i] - pos[0] - vel[0] * times[i] == 0)
        s.add(y + dy * times[i] - pos[1] - vel[1] * times[i] == 0)
        s.add(z + dz * times[i] - pos[2] - vel[2] * times[i] == 0)
    
    m = s.model()
    return str(m.eval(x+y+z))

def check_past(d, f1, sol_x, sol_y):
    (x,y),(dx,dy) = d[f1]
    return (sol_x - x) * dx > 0 and (sol_y - y) * dy > 0 

def p1(day: Input):
    lo = 200000000000000
    hi = 400000000000000
    # lo = 7
    # hi = 27
    dots = parse(day)
    linear = []
    s = 0
    d = {}
    for pos, vel in dots:
        x, y, _ = pos
        dx, dy, _ = vel
        nx, ny = x + dx, y + dy
        a = (y - ny)
        b = (x - nx)*y - a*x
        c = (x - nx)
        d[a,b,c] = ((x,y), (dx,dy))
        linear.append([a,b,c])

    for i,(a,b,c) in enumerate(linear):
        for j,(m,n,o) in enumerate(linear):
            if i >= j: continue
            A = np.array(
                [[-a, c],
                [-m, o]]
            )
            y = np.array([b, n])

            try:
                sol_x, sol_y = np.linalg.solve(A, y)
                if lo <= sol_x <= hi and lo <= sol_y <= hi:
                    if check_past(d, (a,b,c), sol_x, sol_y) and check_past(d, (m,n,o), sol_x, sol_y):
                        s += 1
            except:
                pass
    return s
            


        
