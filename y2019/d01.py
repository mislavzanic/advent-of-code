#!/usr/bin/env python3

def main():
    items = [int(x.strip()) for x in open('input').readlines()]

    def p1(mass: int): return (mass // 3) - 2

    def p2(mass: int):
        s = 0
        while mass > 0:
            if p1(mass) > 0:
                s += p1(mass)
            mass = p1(mass)
        return s
    print(sum(map(p1, items)))
    print(sum(map(p2, items)))

if __name__ == '__main__':
    main()
