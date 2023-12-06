from collections import defaultdict
import sys

bots = defaultdict(set)
bins = defaultdict(set)
chip1, chip2 = 17, 61
p1 = 0
p2 = 0
found1, found2 = False, False
while True:
    for x in open('input').readlines():
        x = x.strip().split()
        if x[0] == 'bot':
            botID = int(x[1])
            lowID = int(x[6])
            highID = int(x[-1])
            if len(bots[botID]) >= 2:
                m, M = min(bots[botID]), max(bots[botID])
                if m == 17 and M == 61 and not found1:
                    p1 = botID
                    found1 = True
                if x[5] == 'bot':
                    bots[lowID].add(m)
                else:
                    bins[lowID].add(m)
                if x[-2] == 'bot':
                    bots[highID].add(M)
                else:
                    bins[highID].add(M)
                bots[botID].remove(m)
                bots[botID].remove(M)

        else:
            bots[int(x[-1])].add(int(x[1]))
    if len(bins[0]) == 1 and len(bins[1]) == 1 and len(bins[2]) == 1 and not found2:
        a, b, c = bins[0].pop(), bins[1].pop(), bins[2].pop()
        p2 = a * b * c
        found2 = True
    if found1 and found2: break
print(p1, p2)
