#!/usr/bin/env python3

import re
from get_input import get_aoc_input

def parse(l):
    r = []
    for line in l:
        z = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        r.append(list(map(int, list(z.groups()))))
    return r

def parse_containers(lines):
    return list(map(
        lambda i: [x[i] for x in reversed(lines) if x[i].isalpha()],
        [i for i, c in enumerate(lines[-1]) if c.isdigit()]
    ))


def main():
    with get_aoc_input(5, 2022) as f:
        cont, pred =  [x.split('\n') for x in f.read().split('\n\n')]
        stack = parse_containers(cont)
        l = parse(pred)

        def calc(stack, l, f):
            for line in l:
                much, start, end = line
                stack[end - 1] = stack[end - 1] + f(stack[start - 1][-much:])
                stack[start - 1] = stack[start - 1][:-much]
            s = ''
            for item in stack:
                if len(item) > 0: s += item[-1]
            return s

        print(calc([x for x in stack], l, lambda x: list(reversed(x))), calc([x for x in stack], l, lambda x: x))


if __name__ == '__main__':
    main()
