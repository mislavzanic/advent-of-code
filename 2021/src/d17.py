import itertools as it
import re
from collections import defaultdict, Counter

def dist(x):
    return x*(x+1) // 2

def f(x,y):
    return (x*(x+1) // 2) - ((x - y - 1)*(x - y) // 2)

def main(l):
    l = l[0]
    m = re.match(r'target area: x=(\d+)..(\d+), y=-(\d+)..-(\d+)',l)
    x1,x2 = int(m.group(1)), int(m.group(2))
    y1,y2 = -int(m.group(3)), -int(m.group(4))
    arr = []
    seen = set()

    for x in range(0,x2+1):
        for y in range(y1 - 10,200):
            if y > 0:
                newx = dist(x) if x <= y else f(x, y)
                high = dist(y)
                if x > y:
                    temp = [i for i in range(x-y) if x1 <= f(x,i+y+1) <= x2]
                    for i in temp:
                        if high-y2 <= dist(y+i) <= high-y1:
                            seen.add((x,y))
                            arr.append(high)
                            break

                if x1 <= dist(x) <= x2:
                    if any(high-y2 <= dist(i) <= high-y1 for i in range(200)):
                        if (x,y) in seen: continue
                        arr.append(high)
            else:
                temp = [i for i in range(0,200) if -y2 <= f(i-y,i) <= -y1]
                for i in temp:
                    newx = dist(x) if x <= i else f(x,i)
                    if x1 <= newx <= x2:
                        arr.append(0)
                        break



    return max(arr), len(arr)
