import itertools as it
from collections import defaultdict

def sdist(x,y):
    return sum(abs(a - b) for a,b in zip(x,y)), tuple(sorted([abs(a-b) for a,b in zip(x,y)]))


def dist(x,y):
    return sum(abs(a - b) for a,b in zip(x,y)), tuple([abs(a-b) for a,b in zip(x,y)])


def parse(inlist):
    scanners = []
    for line in inlist:
        if line[0:3] == '---':
            scanners.append([])
        elif len(line) == 0:...
        else:
            line = line.split(',')
            scanners[-1].append(tuple(int(x) for x in line))
    return scanners


def calc_dist(s, f):
    d = defaultdict(set)
    for i,c1 in enumerate(s):
        for j,c2 in enumerate(s):
            if i != j: d[c1].add(f(c1,c2))
    return d


def compare(s1,s2,f):
    d1,d2 = calc_dist(s1,f), calc_dist(s2,f)
    pairs = []
    for k1,v1 in d1.items():
        arr = []
        for k2,v2 in d2.items():
            result = v1 & v2
            if len(result) >= 11:
                arr.append((len(result), (k1,k2)))
        if len(arr):
            pairs.append(max(arr, key=lambda x: x[0])[1])
    return pairs


def get_perm(p1, p2):
    d1,d2 = dist(p1[0],p2[0])[1],dist(p1[1],p2[1])[1]
    for p in it.permutations([0,1,2]):
        nd = tuple(d2[x] for x in p)
        if d1 == nd: return p
    return (0,0,0)


def get_transform(pairs):
    p = get_perm(pairs[0], pairs[1])
    assert p != (0,0,0)

    rotation = [[-1,1,-1], [1,1,1], [-1,-1,1],[1,-1,-1], [1,1,-1], [-1,1,1], [1,-1,1], [-1,-1,-1]]

    for r in rotation:
        cs = set()
        for pair in pairs:
            dist_c = tuple(pair[0][i] - r[x] * pair[1][x] for i,x in enumerate(p))
            cs.add(dist_c)
        if len(cs) == 1:
            return cs.pop(),p,r
    assert False, "Haven't found the relative coord"

def transform_point(absolute, relative, perm, rot):
    return tuple(absolute[i] + rot[x] * relative[x] for i,x in enumerate(perm))


def transform(i,j,scanners):
    s1,s2 = scanners[i], scanners[j]
    pairs = compare(s1,s2,sdist)
    if not len(pairs): return None
    t = get_transform(pairs)
    for n,item in enumerate(scanners[j]):
        scanners[j][n] = transform_point(t[0], item, t[1], t[2])
    return t[0]


def main(l):
    scanners = parse(l)
    scan = []
    Q = [0]
    seen = set()
    beacons = set()
    while len(Q) > 0:
        curr = Q.pop()
        if curr in seen: continue
        seen.add(curr)
        for i,s in enumerate(scanners):
            if i in seen: continue
            if (tp := transform(curr,i,scanners)) is not None:
                scan.append(tp)
                Q.append(i)

    for i,scanner in enumerate(scanners):
        beacons = beacons | set(point for point in scanner)
    m = [dist(s1,s2)[0] for (s1,s2) in it.combinations(scan,2)]
    return len(beacons), max(m)
