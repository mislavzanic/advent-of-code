from collections import defaultdict
from aoc_util.advent import Input
from aoc_util.search import diff_loop

def connects(pipe1, pipe2, pipes):
    i,j = pipe1
    k,l = pipe2
    match (i - k, j - l):
        case (1,0):
            return pipes[i][j] in ['S', '|', 'J', 'L'] and pipes[k][l] in ['S', '|', '7', 'F']
        case (-1,0):
            return pipes[i][j] in ['S', '|', '7', 'F'] and pipes[k][l] in ['S', '|', 'J', 'L']
        case (0,1):
            return pipes[i][j] in ['S', '-', '7', 'J'] and pipes[k][l] in ['S', '-', 'L', 'F']
        case (0,-1):
            return pipes[i][j] in ['S', '-', 'L', 'F'] and pipes[k][l] in ['S', '-', '7', 'J']
        case _:
            return False

def flood_search(start, pipes, search_type=0):
    check = [(start, int(0))]
    loop = defaultdict(int)
    while check:
        (i, j), length = check.pop(search_type)
        if (i,j) in loop.keys(): continue
        if i == start[0] and j == start[1] and length > 0: break
        loop[(i,j)] = length
        if 0 < i and connects((i,j), (i-1,j), pipes):
            check.append(((i-1,j), length+1))
        if i < len(pipes) - 1 and connects((i,j),(i+1,j), pipes):
            check.append(((i+1,j), length+1))
        if 0 < j and connects((i,j), (i,j-1), pipes):
            check.append(((i,j-1), length+1))
        if j < len(pipes[0])-1 and connects((i,j), (i,j+1), pipes):
            check.append(((i,j+1), length+1))
    return loop

def p2(day: Input):
    loop = defaultdict(int)
    pipes = defaultdict(str)
    for i,line in enumerate(day.lines()):
        for j,c in enumerate(line):
            pipes[(i,j)] = c
            if c == 'S':
                loop = flood_search((i,j), pipes=day.lines(), search_type=-1)
    loop_coord = list(reversed(list(loop.keys())))
    inside = set()

    def check_inside(p1, p2, left):
        di, dj = p1[0] - p2[0], p1[1] - p2[1]
        looking = left[(di,dj)]
        if (p1[0] + looking[0],p1[1] + looking[1]) not in loop.keys():
            if 0 <= p1[0] + looking[0] < len(day.lines()) and 0 <= p1[1] + looking[1] < len(day.lines()[0]):
                inside.add((p1[0] + looking[0],p1[1] + looking[1]))

    for i,point in enumerate(loop_coord):
        check_inside(point, loop_coord[(i+1)%len(loop_coord)], left={(-1,0):(0,1), (1,0):(0,-1), (0,-1): (-1,0), (0,1): (1,0)})
        if pipes[point] in ['F', 'J', '7', 'L']:
            check_inside(point, loop_coord[(i-1)%len(loop_coord)], left={(-1,0):(0,-1), (1,0):(0,1), (0,-1): (1,0), (0,1): (-1,0)})

    Q = [x for x in inside]
    seen = set()
    while Q:
        curr = Q.pop()
        if curr in loop_coord: continue
        if curr in seen: continue
        seen.add(curr)
        inside.add(curr)
        for (di,dj) in diff_loop():
            if abs(di+dj) != 1: continue
            Q.append((curr[0] + di, curr[1] + dj))
    return len(inside)

def p1(day: Input):
    loop = defaultdict(int)
    for i,line in enumerate(day.lines()):
        for j,c in enumerate(line):
            if c == 'S':
                loop = flood_search((i,j), pipes=day.lines())
    return max(loop.values())
    
