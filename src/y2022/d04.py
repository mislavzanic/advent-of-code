#!/usr/bin/env python3

def main():
    l = [x.strip() for x in open('d04.in').readlines()]
    p1, p2 = 0, 0
    for line in l:
        new_l = line.split(',')
        xy = list(map(int, new_l[0].split('-')))
        wz = list(map(int, new_l[1].split('-')))
        p1 += all(xy[0] <= i <= xy[1] for i in range(wz[0], wz[1] + 1)) or all(wz[0] <= i <= wz[1] in wz for i in range(xy[0], xy[1] + 1))
        p2 += any(xy[0] <= i <= xy[1] for i in range(wz[0], wz[1] + 1)) or any(wz[0] <= i <= wz[1] in wz for i in range(xy[0], xy[1] + 1))
    print(p1, p2)

if __name__ == '__main__':
    main()
