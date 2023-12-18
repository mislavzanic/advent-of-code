import itertools
from aoc_util.advent import Input
from aoc_util.search import diff_loop

def parse(lines, parser):
    directions = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    coords = {c:1 for c in itertools.accumulate(
        map(lambda l: parser(*l.split()), lines),
        lambda acc, ni: (
            acc[0] + (directions[ni[0]][0] * ni[1]),
            acc[1] + (directions[ni[0]][1] * ni[1])
        ),
        initial=(0,0)
    )}
    cx = sorted(set(
        [c[0] for c in coords.keys()] +
        [c[0] + 1 for i,c in enumerate(coords.keys()) if i < len(coords.keys()) - 1]
    ))
    cy = sorted(set(
        [c[1] for c in coords.keys()] +
        [c[1] + 1 for i,c in enumerate(coords.keys()) if i < len(coords.keys()) - 1]
    ))
    return list(coords.keys()), {x:i for i,x in enumerate(cx)}, {x:i for i,x in enumerate(cy)}

def dig(instr, coord_x_map, coord_y_map):
    hole = {}
    for i in range(len(instr)):
        x, y = instr[i]
        nx, ny = instr[((i+1) % len(instr))]
        map_x, map_y = coord_x_map[x], coord_y_map[y]
        n_map_x, n_map_y = coord_x_map[nx], coord_y_map[ny]
        for j in range(min(map_x,n_map_x), max(map_x,n_map_x) + 1):
            hole[j,n_map_y] = 1
        for j in range(min(map_y,n_map_y), max(map_y,n_map_y) + 1):
            hole[n_map_x,j] = 1


    inside = {(coord_x_map[0] + 1, coord_y_map[0] + 1)}
    while inside:
        x,y = inside.pop()
        if (x,y) in hole: continue
        hole[x,y] = 1
        for (i,j) in diff_loop():
            if (x+i,y+j) in hole: continue
            inside.add((x+i,y+j))

    s = []
    r_x_map = {v:k for k,v in coord_x_map.items()}
    r_y_map = {v:k for k,v in coord_y_map.items()}

    Mx = max(hole.keys(), key=lambda x: x[0])[0] + 1
    My = max(hole.keys(), key=lambda x: x[1])[1] + 1

    for i in range(0, Mx):
        a = 1 if i+1 not in r_x_map else abs(r_x_map[i] - r_x_map[i+1])
        for j in range(0, My):
            if (i,j) not in hole: continue
            b = 1 if j+1 not in r_y_map else abs(r_y_map[j] - r_y_map[j+1])
            s.append(a * b)
    return sum(s)

def p2(day: Input):
    return dig(*parse(day.lines(), lambda _,b,c: ({'0': 'R', '1':'D', '2':'L', '3': 'U'}[c[-2]], int(c[2:-2], 16))))


def p1(day: Input):
    return dig(*parse(day.lines(), lambda a,b,_: (a,int(b))))
