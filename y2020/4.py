import sys
from collections import defaultdict

def inRange(x, lo, hi):
    return lo <= int(x) <= hi

l = [x.strip() for x in open('input').readlines()]

pas = []
p = []
for x in l:
    x = x.split()
    if x == []:
        pas.append(p)
        p = []
    else:
        for c in x:
            p.append(c)
pas.append(p)
num = 0
num1 = 0
for p in pas:
    passport = {}
    for x in p:
        passport[x[:3]] = x[4:]
    valid1 = all([f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
    if valid1:
        num1 += 1
        valid2 = True
        if valid2:
            valid2 = inRange(passport['byr'], 1920, 2002)
        if valid2:
            valid2 = inRange(passport['iyr'], 2010, 2020)
        if valid2:
            valid2 = inRange(passport['eyr'], 2020, 2030)
        if valid2:
            if passport['hgt'].endswith('in'):
                valid2 = inRange(passport['hgt'][:-2], 59, 76)
            elif passport['hgt'].endswith('cm'):
                valid2 = inRange(passport['hgt'][:-2], 150, 193)
            else: valid2 = False
        if valid2:
            valid2 = not (passport['hcl'][0] != '#' or any([c not in '0123456789abcdef' for c in passport['hcl'][1:]]))
        if valid2:
            valid2 = not (len(passport['pid']) != 9 or any([c not in '0123456789' for c in passport['pid']]))
        if valid2:
            valid2 = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if valid2: 
            num += 1
            print(p)
            
print(num, num1)
