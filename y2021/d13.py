from collections import Counter

def fold(d, f):
    x,y = f
    dd = Counter()
    for k,v in d.items():
        i,j = k
        if y != 0:
            if j > y:
                dd[(i,2*y - j)] = v
                dd[(i,j)] = 0
            else:
                dd[k] = v
        else:
            if i > x:
                dd[(2*x - i,j)] = v
                dd[(i,j)] = 0
            else:
                dd[k] = v
    return sum(v for v in dd.values()), dd

def main(l):
    folds = []
    f = False
    d = Counter()
    for line in l:
        if not len(line):
            f = True
            continue
        if f:
            line = line.split(" ")
            line = (int(line[2][2:]), 0) if line[2][0] == 'x' else (0,int(line[2][2:]))
            folds.append(line)
        else:
            x,y = line.split(',')
            d[(int(x), int(y))] = 1
    part1 = 0
    for i,f in enumerate(folds):
        s, d = fold(d, f)
        if not i: part1 = s
    for i in range(6):
        st = ''
        for j in range(50):
            st += '#' if d[(j,i)] else ' '
        print(st)
    return part1
