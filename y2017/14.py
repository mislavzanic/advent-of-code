from collections import deque

def part1(lens, index, skip, l):
    d = deque(l)

    for x in lens:
        d.rotate(-index)
        l = list(d)
        l1 = l[:x]
        l1.reverse()
        l = l1 + l[x:]
        d = deque(l)
        d.rotate(index)
        index = (index + x + skip) % len(l)
        skip += 1

    return list(d), index, skip

def part2(lens):
    skip, index = 0, 0
    l = [i for i in range(256)]
    for i in range(64):
        l, index, skip = part1(lens, index, skip, l)

    l1 = []
    for i in range(16):
        for j in range(1, 16):
            l[16 * i] = l[16 * i] ^ l[16 * i + j]
        l1.append(hex(l[16 * i]))
    for i in range(len(l1)):
        if len(l1[i][2:]) == 1:
            l1[i] = '0' + l1[i][2:]
        else:
            l1[i] = l1[i][2:]

    return ''.join(l1)

inp = 'ljoxqyyw'
num = 0
unseen = []
for i in range(128):
    string = inp + '-' + str(i)
    asci = [ord(x) for x in string]
    asci += [17, 31, 73, 47, 23]
    h = part2(asci)
    b = bin(int(h, 16))[2:].zfill(128)
    unseen += [(i, j) for j, d in enumerate(b) if d == '1']

count = 0
while unseen:
    queue = [unseen[0]]
    count += 1
    while queue:
        (x, y) = queue.pop()
        if (x, y) in unseen:
            unseen.remove((x, y))
            queue += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
print(count)



