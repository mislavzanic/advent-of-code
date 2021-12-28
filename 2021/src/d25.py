import itertools as it
import re
from collections import defaultdict

def main(l):
    d = defaultdict(str)
    for i,line in enumerate(l):
        s = ''
        for j,char in enumerate(line):
            d[(i,j)] = char
            s += char
        print(s)
    print()

    step = 0
    while True:
        c = False
        dd = defaultdict(str)

        for i in range(len(l)):
            for j in range(len(l[i])):
                dd[(i,j)] = d[(i,j)]

        for i in range(len(l)):
            for j in range(len(l[i])):
                if d[(i,j)] == '>':
                    if j == len(l[i]) - 1 and d[(i,0)] == '.':
                        dd[(i,j)] = '.'
                        dd[(i,0)] = '>'
                        c = True
                    if j < len(l[i]) - 1 and d[(i,j+1)] == '.':
                        dd[(i,j)] = '.'
                        dd[(i,j+1)] = '>'
                        c = True

        for i in range(len(l)):
            for j in range(len(l[i])):
                d[(i,j)] = dd[(i,j)]

        for i in range(len(l)):
            for j in range(len(l[i])):
                if d[(i,j)] == 'v':
                    if i == len(l) - 1 and d[(0,j)] == '.':
                        dd[(i,j)] = '.'
                        dd[(0,j)] = 'v'
                        c = True
                    if i < len(l) - 1 and d[(i+1,j)] == '.':
                        dd[(i,j)] = '.'
                        dd[(i+1,j)] = 'v'
                        c = True

        if not c:
            break
        else:
            for i in range(len(l)):
                for j in range(len(l[i])):
                    d[(i,j)] = dd[(i,j)]
        step += 1
    return step + 1
