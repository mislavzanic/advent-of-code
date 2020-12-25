import re
import fileinput
from collections import defaultdict

def part1(valid, nearby):
    false = []
    p2 = []
    for i,n in enumerate(nearby):
        invalid = False
        for j,nn in enumerate(n):
            found = False
            for v in valid.values():
                if v[0][0] <= nn <= v[0][1] or v[1][0] <= nn <= v[1][1]:
                    found = True
                    break
            if not found:
                false.append(nn)
                invalid = True
        if not invalid:
            p2.append(n)
    print(sum(false))
    return p2


def part2(p2, string, valid, my):
    p = 1
    fields = []
    for i in range(len(my)):
        S = set([c for c in valid.keys()])
        for ticket in p2:
            temp = set()
            for k,v in valid.items():
                if v[0][0] <= ticket[i] <= v[0][1] or v[1][0] <= ticket[i] <= v[1][1]:
                    temp.add(k)
            S = S.intersection(temp)
        fields.append(set([c for c in S]))
    for i,field_one in enumerate(fields):
        for j,field_two in enumerate(fields):
            if i != j and len(field_one) < len(field_two):
                fields[j] = fields[j].difference(field_one)
    for i,field in enumerate(fields):
        for cat in field:
            if string in cat:
                p *= my[i]
    print(p)



lines = [x for x in list(fileinput.input())]
inlist = [defaultdict(list), [], []]
index = 0
for line in lines:
    ints = [int(x) for x in re.findall('-?\d+', line)]
    line = line.split()
    if line and (line[0] == 'your' or line[0] == 'nearby'):
        index += 1
    if ints:
        if not index:
            if line[0] == 'departure' or line[0] == 'arrival':
                inlist[index][line[0]+line[1]] = [[ints[0], -ints[1]],[ints[2],-ints[3]]]
            else:
                inlist[index][line[0]] = [[ints[0], -ints[1]],[ints[2],-ints[3]]]
        elif index == 1:
            inlist[index] = [x for x in ints]
        else:
            inlist[index].append([x for x in ints])

part2(part1(inlist[0], inlist[2]), 'departure', inlist[0], inlist[1])

            
            
