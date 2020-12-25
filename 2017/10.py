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
        l1[i] = l1[i][2:]
    print(''.join(l1))


asci = [ord(x) for x in open('input').readline().strip()]
asci += [17, 31, 73, 47, 23]
part2(asci)
