from aoc_util.advent import Input
import itertools as it

def bfs(start, garden, X, Y, extra_check=None):
    seen = {}
    Q = [(start, 0)]
    while Q:
        curr, steps = Q.pop(0)
        if curr in seen: continue
        seen[curr] = steps
        for (i,j) in it.product([-1,0,1], [-1,0,1]):
            if abs(i+j) != 1: continue
            x,y = curr
            if 0 <= x+i < X and 0 <= j+y < Y:
                if garden[x+i,y+j] == '#': continue
                if extra_check != None:
                    if extra_check(start, garden, X, Y, x+i, y+j): continue
                Q.append(((x+i, y+j), steps + 1))
    return seen

def parse(day: Input):
    garden = {}
    start = (0,0)
    for i, line in enumerate(day.lines()):
        for j, char in enumerate(line):
            if char == 'S': start = (i,j)
            garden[i,j] = char
    return start, garden, len(day.lines()), len(day.lines()[0])

def p2(day: Input):
    start, garden, X, Y = parse(day)
    N = 26501365
    steps = bfs(start, garden, X, Y)
    radius = (N // X) + 1

    odd_boards = 4 * sum(i for i in range(radius - 1) if i % 2 == 0 and i > 0) + 1
    even_boards = 4 * sum(i for i in range(radius - 1) if i % 2 == 1)

    even_coords = sum(1 for k in steps if (start[0] + start[1]) % 2 == (k[0] + k[1]) % 2)
    odd_coords = sum(1 for k in steps if (start[0] + start[1]) % 2 != (k[0] + k[1]) % 2)
    odd_corners = sum(1 for k in steps if abs(k[0] - start[0]) + abs(k[1] - start[1]) > 65 and (start[0] + start[1]) % 2 != (k[0] + k[1]) % 2)
    even_corners = sum(1 for k in steps if abs(k[0] - start[0]) + abs(k[1] - start[1]) > 65 and (start[0] + start[1]) % 2 == (k[0] + k[1]) % 2)
    s = (odd_boards * odd_coords + even_boards * even_coords)
    s += ((4*radius - 8) * odd_coords) - ((radius - 2) * odd_corners)
    s += even_corners * (radius - 1)
    s += 4 * odd_coords - (2 * odd_corners)
    return s


def p1(day: Input):
    steps = bfs(*parse(day))
    return sum(1 for x in steps.values() if x % 2 == 64 % 2 and x <= 64)
