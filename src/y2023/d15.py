from aoc_util.advent import Input
from collections import Counter

def f(char, value):
    return (17 * (value + ord(char))) % 256

def HASH(string):
    v = 0
    for c in string:
        v = f(c,v)
    return v
        
def p2(day: Input):
    inp = day.string().strip().split(',')
    box = [Counter() for _ in range(256)]
    for lens in inp:
        if lens[-1] == '-':
            h = HASH(lens[:-1])
            if lens[:-1] in box[h]:
                del box[h][lens[:-1]]
        else:
            s, val = lens.split('=')
            h = HASH(s)
            box[h][s] = int(val)
                
    s = 0
    for i,item in enumerate(box):
        for j,key in enumerate(item.keys()):
            s += (i + 1) * (j+1) * (item[key])
    return s
            
def p1(day: Input):
    inp = day.string().strip().split(',')
    s = 0
    for line in inp:
        s += HASH(line)
    return s
