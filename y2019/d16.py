#!/usr/bin/env python3

from collections.abc import Generator


def main():
    l = list(map(int, [x for x in open('input').readline().strip()]))
    offset = int(''.join(map(str,l[:7])))
    n = len(l)

    def pattern(n: int, length: int) -> Generator:
        much, current, prev = n - 1, 0, -1
        for _ in range(length):
            if much == 0:
                much, ncurrent, nprev = n, prev if prev == 0 else current - prev, current
                current, prev = ncurrent, nprev
            much -= 1
            yield current

    def part1(n, l):
        matrix = [[x for x in pattern(i + 1, len(l))] for i in range(n)]

        for _ in range(100):
            l = [int(str(sum(map(lambda p: p[0] * p[1], zip(l, row))))[-1]) for row in matrix]
        print(''.join([str(x) for x in l[:8]]))

    def part2(offset, n):
        m = (n * 10000) - offset
        repeat = (m - (m % n)) // n
        temp = [int(x) for x in open('input').readline().strip()]
        l = temp[n - (m % n):] + (temp * repeat)
        assert(len(l) == m)

        def sums(l: list[int], m: int) -> list[int]:
            new_l = [sum(l)]
            for i in range(m):
               new_l.append(new_l[i] - l[i])
            return new_l

        for _ in range(100):
            l = sums(l, m)
            l = [x % 10 for x in l]
        print(''.join([str(x) for x in l[:8]]))


    part2(offset, n)


if __name__ == '__main__':
    main()
