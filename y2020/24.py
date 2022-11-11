import fileinput
from collections import defaultdict 

def reduce(tile):
    tile = list(tile)
    if tile[5] >= tile[4] > 0:
        tile[1] += tile[4]
        tile[5] -= tile[4]
        tile[4] = 0
    elif tile[4] > tile[5] > 0:
        tile[1] += tile[5]
        tile[4] -= tile[5]
        tile[5] = 0

    if tile[3] >= tile[2] > 0:
        tile[0] += tile[2]
        tile[3] -= tile[2]
        tile[2] = 0
    elif tile[2] > tile[3] > 0:
        tile[0] += tile[3]
        tile[2] -= tile[3]
        tile[3] = 0

    if tile[3] >= tile[4]:
        tile[3] -= tile[4]
        tile[4] = 0
    else:
        tile[4] -= tile[3]
        tile[3] = 0

    if tile[5] >= tile[2]:
        tile[5] -= tile[2]
        tile[2] = 0
    else:
        tile[2] -= tile[5]
        tile[5] = 0

    if tile[0] >= tile[1]:
        tile[0] -= tile[1]
        tile[1] = 0
    else:
        tile[1] -= tile[0]
        tile[0] = 0

    if tile[0] >= tile[4] > 0:
        tile[2] += tile[4]
        tile[0] -= tile[4]
        tile[4] = 0
    elif tile[4] > tile[0] > 0:
        tile[2] += tile[0]
        tile[4] -= tile[0]
        tile[0] = 0

    if tile[0] >= tile[5] > 0:
        tile[3] += tile[5]
        tile[0] -= tile[5]
        tile[5] = 0
    elif tile[5] > tile[0] > 0:
        tile[3] += tile[0]
        tile[5] -= tile[0]
        tile[0] = 0

    if tile[1] >= tile[3] > 0:
        tile[5] += tile[3]
        tile[1] -= tile[3]
        tile[3] = 0
    elif tile[3] > tile[1] > 0:
        tile[5] += tile[1]
        tile[3] -= tile[1]
        tile[1] = 0

    if tile[1] >= tile[2] > 0:
        tile[4] += tile[2]
        tile[1] -= tile[2]
        tile[2] = 0
    elif tile[2] > tile[1] > 0:
        tile[4] += tile[1]
        tile[2] -= tile[1]
        tile[1] = 0
    tile = tuple(tile)
    return tile


lines = [x.strip() for x in fileinput.input()]
black = defaultdict(int)
for line in lines:
    tile = defaultdict(int)
    i = 0
    while i < len(line):
        c = line[i]
        if c == 'n' or c == 's':
            tile[c + line[i+1]] += 1
            i += 1
        else:
            tile[c] += 1
        i += 1
    
    key = (tile['e'], tile['w'], tile['ne'], tile['se'], tile['nw'], tile['sw'])
    key = reduce(key)
    black[key] += 1
    black[key] %= 2

print(sum(black.values()))
for j in range(100):
    bb = defaultdict(int)
    for k,v in black.items():
        bb[k] = v
        for i in range(6):
            tempk = list(k)
            tempk[i] += 1
            tempk = tuple(tempk)
            tempk = reduce(tempk)
            bb[tempk] = bb[tempk]
    for k,v in bb.items():
        numofb = 0
        for i in range(6):
            tempk = list(k)
            tempk[i] += 1
            tempk = tuple(tempk)
            tempk = reduce(tempk)
            numofb += bb[tempk]
        if bb[k] and (numofb == 0 or numofb > 2):
            black[k] = 0
        elif not bb[k] and numofb == 2:
            black[k] = 1
    print(j, sum(black.values()))
print(sum(black.values()))
