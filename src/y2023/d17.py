from aoc_util.advent import Input
from queue import PriorityQueue

'''
970 -> too high
p2 1105 -> to high
p2 1104 -> to high
'''

def dijkstra(matrix, turn_condition, stop_condition):
    Q = PriorityQueue()
    Q.put((0, 0,0,(1,0),0))
    Q.put((0, 0,0,(0,1),0))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = set()
    while Q:
        heat, x, y, direction, steps = Q.get()
        key = (x,y,direction,steps)
        if key in seen: continue
        seen.add(key)
        if stop_condition(steps) and (x,y) == (len(matrix)-1, len(matrix[0]) - 1):
            return heat
        for (dx,dy) in dirs:
            if not (0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[x])): continue
            if (-dx,-dy) == direction: continue
            if not turn_condition((dx,dy), direction, steps): continue
            new_key = (x+dx,y+dy,(dx,dy),1 if (dx,dy) != direction else steps+1)
            Q.put((heat + matrix[x+dx][y+dy], *new_key))
    return None



def p2(day: Input):
    return dijkstra(
        matrix=[[int(c) for c in line] for line in day.lines()],
        turn_condition=lambda d1, d2, s: (d1 == d2 and s < 10) or (d1 != d2 and s >= 4),
        stop_condition=lambda s: 10 >= s >= 4
    )

def p1(day: Input):
    return dijkstra(
        matrix=[[int(c) for c in line] for line in day.lines()],
        turn_condition=lambda d1, d2, s: (d1 != d2 or s < 3),
        stop_condition=lambda _: True
    )
