from aoc_util.advent import Input

def parse(day: Input):
    l = day.lines()
    empty_row, empty_col = [], []
    galaxy = []
    for i, _ in enumerate(day.lines()):
        if all(l[i][y] == '.' for y,_ in enumerate(l[i])):
            empty_row.append(i)
    
    for j, _ in enumerate(day.lines()[0]):
        if all(l[x][j] == '.' for x,_ in enumerate(l)):
            empty_col.append(j)

    for i,line in enumerate(l):
        for j,c in enumerate(line):
            if c == '#': galaxy.append((i,j))
    return galaxy, empty_row, empty_col

def calc_diff(dist, galaxy, empty_row, empty_col):
    s = 0
    for i,g1 in enumerate(galaxy):
        for j,g2 in enumerate(galaxy):
            if i <= j: continue
            diff_row = (dist-1) * sum(1 for x in empty_row if min(g2[0],g1[0]) <= x <= max(g2[0],g1[0]))
            diff_col = (dist-1) * sum(1 for x in empty_col if min(g2[1],g1[1]) <= x <= max(g2[1],g1[1]))
            s += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]) + diff_row + diff_col
    return s

def p2(day: Input):
    return calc_diff(1000000, *parse(day))

def p1(day: Input):
    return calc_diff(2, *parse(day))

