import itertools as it

def part1(l):
    return sum(l[i] < l[i+1] for i in range(len(l) - 1))


def part2(l):
    ll = [sum(l[i:i+3]) for i in range(len(l))]
    return sum(ll[i] < ll[i+1] for i in range(len(l) - 2))
