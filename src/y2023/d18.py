from functools import reduce
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

def dig(coords, coord_x_map, coord_y_map):
    mapped_coords = map(
       lambda pair: (
           (coord_x_map[pair[0][0]], coord_y_map[pair[0][1]]),
           (coord_x_map[pair[1][0]], coord_y_map[pair[1][1]])
       ),
       zip(coords, coords[1:] + [coords[0]])
    )

    def fill(d):
        inside = {(coord_x_map[0] + 1, coord_y_map[0] + 1)}
        while inside:
            x,y = inside.pop()
            if (x,y) in d: continue
            d[x,y] = 1
            for (i,j) in diff_loop():
                if (x+i,y+j) in d: continue
                inside.add((x+i,y+j))
        return d

    hole = fill(reduce(
        lambda x, y: x | y, [{
            (j,ny):1 for j in range(min(x,nx), max(x,nx) + 1)
        } | {
            (nx,j):1 for j in range(min(y,ny), max(y,ny) + 1)
        } for ((x,y), (nx,ny)) in mapped_coords]
    ))

    s = []
    rx_map = {v:k for k,v in coord_x_map.items()}
    ry_map = {v:k for k,v in coord_y_map.items()}

    Mx = max(hole.keys(), key=lambda x: x[0])[0] + 1
    My = max(hole.keys(), key=lambda x: x[1])[1] + 1

    return sum(
        (1 if i+1 not in rx_map else abs(rx_map[i] - rx_map[i+1])) *
        (1 if j+1 not in ry_map else abs(ry_map[j] - ry_map[j+1]))
        for i in range(0, Mx)
        for j in range(0,My)
        if (i,j) in hole
    )

def p2(day: Input):
    return dig(*parse(day.lines(), lambda _,b,c: ({'0': 'R', '1':'D', '2':'L', '3': 'U'}[c[-2]], int(c[2:-2], 16))))


def p1(day: Input):
    return dig(*parse(day.lines(), lambda a,b,_: (a,int(b))))
