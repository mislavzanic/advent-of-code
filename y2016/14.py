from collections import deque
from collections import defaultdict
import sys
from hashlib import md5

salt = 'jlmsuwbz'
keys = 64

i = 0
tocheck = []
keylist = []
while keys > 0:

    for item in tocheck:
        if item[1] - 1 < 0:
            tocheck.remove(item)

    for j in range(len(tocheck)):
        tocheck[j][1] -= 1
    a = salt + str(i)
    for k in range(2017):
        a = md5(a.encode()).hexdigest()
    t = a
    char = None
    charlist = []
    for j in range(len(t) - 2):
        if t[j] == t[j+1] == t[j+2] and char == None:
            char = t[j]
        if j < len(t) - 5:
            if t[j] == t[j+1] == t[j+2] == t[j+3] == t[j+4]:
                charlist.append(t[j])
    toremove = []
    for items in tocheck:
        for c in charlist:
            if items[0] == c and items not in toremove:
                keys -= 1
                keylist.append(items[2])
                if keys == 0:
                    print(keylist[63])
                toremove.append(items)
    for item in toremove:
        tocheck.remove(item)
    if char != None:
        tocheck.append([char, 1000, i])
    i += 1
