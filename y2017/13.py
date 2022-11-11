d = dict()
     
for x in open('input').readlines():
    x = x.strip()
    num1, num2 = int(x[:x.find(':')]), int(x[x.find(' '):])
    d[num1] = num2
     
def part1():
    caught = list()
    scanner = {i:0 for i in d.keys()}
    direction = {i:'+' for i in d.keys()}
    for packet in range(max(d.keys()) + 1):
        if packet in d.keys():
            if scanner[packet] == 0:
                caught.append(packet * d[packet])
        for i in scanner.keys():
            if scanner[i] == d[i] - 1:
                direction[i] = '-'
            elif scanner[i] == 0:
                direction[i] = '+'
            if direction[i] == '-':
                scanner[i] -= 1
            else:
                scanner[i] += 1

def part2():
    times = list()
    delays = list()
    for k, v in d.items():
        times.append(2 * (v - 1))
        delays.append(k)
    i = 1000000
    notFound = False
    while True:
        for j in range(len(times)):
            if (i + delays[j]) % times[j] == 0:
                notFound = True
                break
        if not notFound:
            print(i)
            break
        else:
            notFound = False
            i += 1
part2()
