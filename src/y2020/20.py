import math
import fileinput
from collections import defaultdict
import re

def removeBorder(A):
    temp = [[None for _ in range(len(A[1])-2)] for _ in range(len(A)-2)]
    for i in range(1,len(A)-1):
        for j in range(1,len(A[i])-1):
            temp[i-1][j-1] = A[i][j]
    return temp


def printmat(A):
    for r in A: print(r)
    print(' ')

def copy(matrix):
    return [[c for c in r] for r in matrix]

def equ(A, B):
    for i in range(len(A)):
        if A[i] != B[i]: return False
    return True

def flip(matrix):
    N = len(matrix)
    M = len(matrix[0])
    for x in range(N):
        for y in range(M // 2):
            matrix[x][y], matrix[x][M-y-1] = matrix[x][M - y - 1],matrix[x][y]
    return matrix

def rflip(matrix):
    N = len(matrix)
    M = len(matrix[0])
    for x in range(N//2):
        for y in range(M):
            matrix[x][y], matrix[N-x-1][y] = matrix[N-x-1][y],matrix[x][y]
    return matrix

def lrotate(matrix):
    N = len(matrix)
    for x in range(N // 2):
        for y in range(x, N - x - 1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = matrix[N - 1 - x][N - 1 - y]
            matrix[N - 1 - x][N - 1 - y] = matrix[N - 1 - y][x]
            matrix[N - 1 - y][x] = tmp
    return matrix

def rrotate(matrix):
    return lrotate(lrotate(lrotate(matrix)))

def flipRow(row):
    N = len(row)
    for i in range(N//2):
        row[i], row[N-i-1] = row[N-i-1], row[i]
    return row

def match(m1, m2, i, j):
    flipi, flipj = False, False
    if i > 3: flipi = True
    if j > 3: flipj = True

    tempi = i if i < 4 else i - 4
    tempj = j if j < 4 else j - 4

    while tempi:
        m1 = lrotate(m1)
        tempi -= 1
    while tempj:
        m2 = lrotate(m2)
        tempj -= 1
    if flipi: m1 = flip(m1)
    if flipj: m2 = flip(m2)
    assert equ(m1[0],m2[0]) 
    m1 = rrotate(m1)
    m2 = rflip(lrotate(m2))
    return m1, m2

def search(img):
    num = 0
    for i in range(len(img)-2):
        for j in range(len(img[i])-20):
            if img[i][j+18] == '#':
                ok = True
                for k in [0,5,6,11,12,17,18,19]:
                    if img[i+1][j+k] != '#':
                        ok = False
                        break
                if not ok:
                    continue    
                else:
                    for k in [1,4,7,10,13,16]:
                        if img[i+2][j+k] != '#':
                            ok = False
                            break
                    if not ok:
                        continue
                    else:
                        num += 1
                        img[i][j+18] = 'O'
                        for k in [0,5,6,11,12,17,18,19]:
                            img[i+1][j+k] = 'O'
                        for k in [1,4,7,10,13,16]:
                            img[i+2][j+k] = 'O'
    return num

def p1(tiles, dim):
    matches = defaultdict(int)
    temp = defaultdict(list)
    seen = set()
    for i,t in enumerate(tiles.items()):
        for j,tt in enumerate(tiles.items()):
            id1,image1 = t
            id2,image2 = tt
            if id1 != id2 and (id1,id2) not in seen:
                seen.add((id1, id2))
                seen.add((id2, id1))
                cand1 = [None for _ in range(8)]
                cand2 = [None for _ in range(8)]
                for kk in range(4):
                    cand1[kk] = [c for c in image1[0]]
                    cand2[kk] = [c for c in image2[0]]
                    cand1[kk+4] = flipRow([c for c in image1[0]])
                    cand2[kk+4] = flipRow([c for c in image2[0]])
                    image1 = lrotate(image1)
                    image2 = lrotate(image2)
                found = False
                for i,c1 in enumerate(cand1):
                    for j,c2 in enumerate(cand2):
                        if equ(c1, c2):
                            found = True
                            matches[id1] += 1
                            matches[id2] += 1
                            temp[id1].append((id2, i, j))
                            temp[id2].append((id1, j ,i))
                            break
                    if found:
                        break
    p = 1
    for k,v in matches.items():
        if v == 2: p*=k
    return p, temp


def p2(tiles, picture, dim):
    img = defaultdict(list)
    seen = set()
    start = (0,0)
    startk = None
    startv = None
    for k,v in picture.items():
        if len(v) == 2:
            startk = k   
            startv = v
            break
    A, B = match(copy(tiles[startk]), copy(tiles[startv[0][0]]), startv[0][1], startv[0][2])
    
    i = 1
    j = 0
    img[(0,0)] = copy(A)
    img[(0,1)] = copy(B)
    seen.add(startk)
    nextid = startv[0][0]
    seen.add(nextid)
    corner = startk
    while j < dim:
        while i < dim-1:
            cands = picture[nextid]
            for cand in cands:
                id_, tempi, tempj = cand
                if id_ in seen:
                    continue
                C, D = match(copy(tiles[nextid]), copy(tiles[id_]), tempi, tempj)
                rotations = 0
                
                while C != img[(j,i)]:
                    if rotations > 0 and rotations % 4 == 0:
                        C, D = flip(C), flip(D)
                    C = lrotate(C)
                    D = lrotate(D)
                    rotations += 1
                if equ(flipRow(lrotate(copy(C))[0]),rrotate(copy(D))[0]):
                    img[(j,i+1)] = copy(D)
                    seen.add(id_)
                    nextid = id_
                    break
            i += 1
        i = 0
        A = copy(img[(j,i)])
        cands = picture[corner]
        for cand in cands:
            id_, tempi, tempj = cand
            if id_ in seen:
                continue
            C, D = match(copy(tiles[corner]),copy(tiles[id_]), tempi, tempj)
            rotations = 0
            while C != img[(j,i)]:
                if rotations > 0 and rotations % 4 == 0:
                    C, D = flip(C), flip(D)
                C = lrotate(C)
                D = lrotate(D)
                rotations += 1
            img[(j+1,i)] = copy(D)
            seen.add(id_)
            corner = nextid = id_
        j += 1
    tempimg = []
    for i in range(dim):
        temp = [[0 for _ in range(8*dim)] for _ in range(8)]
        for j in range(dim):
            img[(i,j)] = removeBorder(img[(i,j)])
            for a,r in enumerate(img[(i,j)]):
                for b,c in enumerate(r):
                    temp[a][b + 8*j] = '#' if c == 1 else ' '
        for r in temp:
            tempimg.append([c for c in r])
    img = tempimg
    rotations = 0
    monster = 0
    while not monster:
        if rotations > 0 and rotations % 4 == 0:
            img = flip(img)
        monster += search(img)
        if monster:
            for r in img: print(''.join(r))
            rough = 0
            for r in img:
                for c in r:
                    if c == '#': rough += 1
            return rough
        img = lrotate(img)
        rotations += 1
                
def main():
    lines = [x for x in fileinput.input()]
    tiles = defaultdict(list)
    currTile = None
    tile = defaultdict(int)
    j = 0
    ID = []
    for line in lines:
        line = line.strip()
        ints = [int(x) for x in re.findall('-?\d+', line)]
        if ints:
            currTile = ints[0]
            ID.append(currTile)
            tile = defaultdict(int)
            j += 1
        elif line:
            temp = []
            for i,c in enumerate(line):
                temp.append(1 if c == '#' else 0)
            tiles[currTile].append([c for c in temp])
    dim = int(math.sqrt(j))
    part1, picture = p1(tiles, dim)
    print(part1)
    part2 = p2(tiles, picture, dim)
    print(part2)
    

if __name__ == '__main__':
    main()
