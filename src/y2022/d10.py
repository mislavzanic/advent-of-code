#!/usr/bin/env python3

from get_input import get_aoc_input

from collections import defaultdict

cycle = 0

def main(example: str):
    l = []
    if example == '':
        with get_aoc_input(10, 2022) as f:
            l = [x.strip() for x in f.readlines()]
    else:
        l = [x.strip() for x in open(example).readlines()]


    X, signal, d = 1, [], defaultdict(str)

    def draw(X, row, col, d):
        for i in [X-1, X, X+1]:
            if i == col:
                d[(row, col)] = '#'
                return
        d[(row, col)] = ' '

    def add_cycle(X, signal):
        global cycle
        cycle += 1
        if (cycle - 20) % 40 == 0: signal.append(cycle * X)

    def do_cycle(X, signal, d):
        global cycle
        add_cycle(X, signal)
        draw(X, cycle // 40, (cycle - 1) % 40, d)

    for cmd in l:
        do_cycle(X, signal, d)
        if cmd != 'noop':
            num = int(cmd.split(' ')[1])
            do_cycle(X, signal, d)
            X += num

    print(sum(signal))
    for i in range(7):
        s = ''
        for j in range(0, 41):
            s += d[(i, j)]
        print(s)



if __name__ == '__main__':
    main('')
    # main('input/10.ex')
