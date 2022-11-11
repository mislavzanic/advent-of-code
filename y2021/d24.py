from collections import Counter

mFREE = {}
MFREE = {}
DEP = {}


def parse(l):
    for i,line in enumerate(l):
        line = line.split()
        l[i] = line
    return l


def analyze(block,zstack,index):
    for line in block:
        if ' '.join(line) == 'div z 1':
            mFREE['w'+str(index)] = 0
            MFREE['w'+str(index)] = 0
            zstack.append(['w'+str(index),int(block[-3][2])])
        elif ' '.join(line) == 'div z 26':
            var = zstack.pop()
            DEP['w'+str(index)] = [var, int(block[5][2])]


def decompile(l):
    zstack = []
    for i in range(14):
        block = []
        block.append(l.pop(0))
        while len(l) > 0 and l[0] != ['inp', 'w']:
            block.append(l.pop(0))
        analyze(block,zstack,i)


def get_min(a,b):
    for i in range(1,10):
        if 10 > i + a + b > 0:
            return i


def get_max(a,b):
    for i in range(9,0,-1):
        if 10 > i + a + b > 0:
            return i


def main(l):
    l = parse(l)
    regs = Counter()
    decompile(l)
    for k in mFREE.keys():
        for kk,vv in DEP.items():
            if vv[0][0] != k: continue
            a,b = vv[0][1],vv[1]
            mFREE[k] = get_min(a,b)
            MFREE[k] = get_max(a,b)
            break
    m,M = ['' for _ in range(14)],['' for _ in range(14)]
    for k in mFREE.keys():
        m[int(k[1:])] = str(mFREE[k])
        M[int(k[1:])] = str(MFREE[k])
    for k,v in DEP.items():
        m[int(k[1:])] = str(v[1] + v[0][1] + mFREE[v[0][0]])
        M[int(k[1:])] = str(v[1] + v[0][1] + MFREE[v[0][0]])
    return int(''.join(M)),int(''.join(m))
