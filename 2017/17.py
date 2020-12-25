def part1():
    inp = 301
    pos = 0
    nextVal = 1
    l = [0]

    while nextVal < 2018:
        pos = (pos + inp) % len(l)
        l.insert(pos + 1, nextVal)
        pos += 1
        nextVal += 1
    print(l[pos + 1])

def part2():
    inp = 301
    pos = 0
    nextVal = 1
    l = [0]
    listlen = 1
    
    while nextVal < 50000001:
        pos = (pos + inp) % listlen
        if pos == 0:
            l.insert(1, nextVal)
        listlen += 1
        pos += 1
        nextVal += 1
    
    print(l[(1)])

part1()
part2()
