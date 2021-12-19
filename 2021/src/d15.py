from collections import defaultdict
from queue import PriorityQueue


def bfs(d, end):
    Q = [(0,0,0)]
    Q = PriorityQueue()
    Q.put((0,0,0))
    seen = set()
    while not Q.empty():
        curr = Q.get();
        s,x,y = curr
        if (x,y) in seen or x < 0 or y < 0 or x > end[0] or y > end[0]: continue
        if (x,y) == end:
            return s
        seen.add((x,y))
        for item in [(s+d[(x-1,y)],x-1,y), (s+d[(x+1,y)],x+1,y), (s+d[(x,y-1)],x,y-1), (s+d[(x,y+1)],x,y+1)]:
            Q.put(item)


def main(l):
    d = defaultdict(int)
    for x in range(5):
        for y in range(5):
            for i,line in enumerate(l):
                for j,char in enumerate(line):
                    if x + y == 0:
                        d[(i + x * len(l),j + y * len(l[0]))] = int(char)
                    elif y > 0:
                        d[(i + x * len(l),j + y * len(l[0]))] = (int(d[(i+x * len(l), j + (y-1) * len(l[0]))]) + 1) % 10
                        if d[(i + x * len(l),j + y * len(l[0]))] == 0: d[(i + x * len(l),j + y * len(l[0]))]+=1
                    elif x > 0:
                        d[(i + x * len(l),j + y * len(l[0]))] = (int(d[(i+(x-1) * len(l), j + y * len(l[0]))]) + 1) % 10
                        if d[(i + x * len(l),j + y * len(l[0]))] == 0: d[(i + x * len(l),j + y * len(l[0]))]+=1

    return bfs(d, (5 * (len(l)) - 1, 5 * (len(l[0])) - 1))
