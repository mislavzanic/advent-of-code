#!/usr/bin/env python3

import itertools as it

def main():
    l = ''.join([x.strip()+"," if len(x.strip()) > 1 else ";" for x in open('input').readlines()])
    ll = list(map(lambda x: sum(map(int, (x[:-1]).split(','))), l.split(';')))
    ll.sort()

    print(ll[-1], sum(ll[-3:]))


if __name__ == '__main__':
    main()
