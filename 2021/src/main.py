import sys
import d1
import d2

if __name__ == '__main__':
    _, day, infile = sys.argv

    inlist = [x.strip() for x in open(infile).readlines()]

    if day == '1':
        inlist = [int(x) for x in inlist]
        print(d1.part1(inlist))
        print(d1.part2(inlist))
    if day == '2':
        print(d2.part1(inlist))
        print(d2.part2(inlist))
    else: raise NotImplementedError()
