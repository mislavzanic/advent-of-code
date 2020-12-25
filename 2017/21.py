from collections import defaultdict
import sys

def flipCol(matrix):
    matrix = matrix.split('/')
    matrix = [[c for c in matrix[k]] for k in range(len(matrix))]
    N = len(matrix)

    for x in range(N):
        for y in range(N // 2):
            matrix[x][y] = matrix[x][N - y - 1]

    matrix = [''.join(matrix[k]) for k in range(len(matrix))]
    matrix = '/'.join(matrix)
    return matrix

def rotate(matrix):
    matrix = matrix.split('/')
    matrix = [[c for c in matrix[k]] for k in range(len(matrix))]
    N = len(matrix)
    for x in range(N // 2):
        for y in range(x, N - x - 1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = matrix[N - 1 - x][N - 1 - y]
            matrix[N - 1 - x][N - 1 - y] = matrix[N - 1 - y][x]
            matrix[N - 1 - y][x] = tmp
    matrix = [''.join(matrix[k]) for k in range(len(matrix))]
    matrix = '/'.join(matrix)
    return matrix

def indict(string):
    found = False
    while not found:
        for j in range(4):
            string = rotate(string)
            if string in d.keys():
                found = True
                break
        if not found:
            string = flipCol(string)
    string = d[string]
    return string


def rec(index, start):
    s = 0
    if index == 6:
        for x in start:
            if x == '#':
                s += 1
        return s
    index += 1
    size = start.find('/')
    print(start, size)
    if size == 2 or size == 3:
        start = indict(start)
        s = rec(index, start)
    elif size % 2 == 0:
        size /= 2
        start = start.split('/')
        start = ''.join(start)
        parts = [['' for _ in range(2)] for _ in range(size * size)]
        for m in range(size):
            for l in range(size):
                for k in range(2):
                    for j in range(2):
                        parts[m * size + l][k] += start[j + k * 2 * size + l * 2 + m * size * 4]
        newstart = ''
        for j in range(size * size):
            temp = ''
            for k in range(2):
                temp += parts[j][k]
                temp += '/'
            newstart += indict(temp[:-1])
            newstart += '/'
        newstart = newstart[:-1]
        s += rec(index, newstart)
    elif size % 3 == 0:
        size /= 3
        start = start.split('/')
        start = ''.join(start)
        parts = [['' for _ in range(3)] for _ in range(size * size)]
        for m in range(size):
            for l in range(size):
                for k in range(3):
                    for j in range(3):
                        parts[m][k] += start[j + 3 * size * k + 3 * l + m * size * 9]
        newstart = ''
        for j in range(size * size):
            temp = ''
            for k in range(3):
                temp += parts[j][k]
                temp += '/'
            newstart += indict(temp[:-1])
            newstart += '/'
        newstart = newstart[:-1]
        newstart = newstart.split('/')
        print(newstart) 
        s += rec(index, newstart)

    return s


d = defaultdict(str)

for x in open('input').readlines():
    x = x.strip()
    a, b = x[:x.find(' ')], x[x.find('>') + 2:]
    d[a] = b

i = 1
start = '.#./..#/###'
print(rec(i, start))        
