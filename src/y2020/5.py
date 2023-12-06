from collections import defaultdict
import sys
l = [x.strip() for x in open('input').readlines()]
seats = set()
for x in l:
    num = ''
    for c in x:
        if c == 'B' or c == 'R':
            num += '1'
        else:
            num += '0'
    seats.add(int(num, 2))

print(max(seats))
for s in seats:
    if s-1 not in seats and s-2 in seats:
        print(s-1)

