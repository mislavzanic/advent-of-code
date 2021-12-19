import re
from collections import defaultdict, Counter
import itertools as it


def main(l):
    d = defaultdict(str)
    corupted = Counter()
    corrupted = {')':3, ']': 57, '}': 1197, '>': 25137}
    correct = {')':1, ']': 2, '}': 3, '>': 4}
    pairs = {']':'[', '}':'{', ')':'(', '>':'<'}
    scores = []
    for line in l:
        depth = 0
        for i,char in enumerate(line):
            if char in pairs.keys():
                pair = pairs[char]
                depth -= 1
                if depth < 0 or d[depth] != pair:
                    corupted[char] += 1
                    break
            else:
                d[depth] = char
                depth += 1

            if i == len(line) - 1:
                revdict = {v:k for k,v in pairs.items()}
                ss = sum(correct[revdict[d[x]]] * (5**x) for x in range(depth))
                scores.append(ss)
    s = sum(v*corrupted[k] for k,v in corupted.items())
    scores.sort()

    return s,scores[len(scores) // 2]
