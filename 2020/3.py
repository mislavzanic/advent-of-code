from collections import defaultdict

d = defaultdict(int)
l = [x.strip() for x in open('input').readlines()]
for i in range(len(l)):
    for j in range(len(l[i])):
        d[tuple((i, j))] = 1 if l[i][j] == '#' else 0

p1 = 0
offsetx, offsety = 1, 1
nums = []
while offsetx < 2 or offsety < 2:
    p1, i, j = 0, 0, 0
    while True:
        i += offsetx
        if not i < len(l):
            if offsety == 3 and offsetx == 1:
                print(p1)
            nums.append(p1)
            break

        p1 += d[tuple((i, (j + offsety)%len(l[0])))]
        j += offsety

    offsety += 2
    if offsety % 9 == 0:
        offsety = 1
        offsetx += 1


p2 = 1
for x in nums:
    p2 *= x
print(p2)
