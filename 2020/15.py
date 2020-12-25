import re
import fileinput
from collections import defaultdict

line = '0,14,6,20,1,4'
ints = [int(x) for x in re.findall('-?\d+',line)]
spoken = defaultdict(int)
turn = defaultdict(list)

last = None
iterations = 30000000
for i in range(iterations):
    if i == 2020:
        print(last)
    if i < len(ints):
        spoken[ints[i]] += 1
        turn[ints[i]].append(i)
        last = ints[i]
    else:
        if spoken[last] == 1:
            spoken[0] += 1
            turn[0].append(i)
            last = 0
        else:
            num = turn[last][len(turn[last]) - 1] - turn[last][len(turn[last]) - 2]
            spoken[num] += 1
            last = num
            turn[num].append(i)
print(last)
