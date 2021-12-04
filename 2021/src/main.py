import sys
import d1
import d2
import d3
import d4

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
    if day == '3':
        print(d3.part1(inlist))
        print(d3.part2(inlist))
    if day == '4':
        print(d4.part1(inlist))
    else: raise NotImplementedError()
