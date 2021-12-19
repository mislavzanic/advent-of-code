import sys
import d1
import d2
import d3
import d4
import d5
import d6
import d7
import d8
import d9
import d10
import d11
import d12
import d13
import d14
import d15
import d16
import d17
import d18
import d19

if __name__ == '__main__':
    _, day, infile = sys.argv

    inlist = [x.strip() for x in open(infile).readlines()]

    if day == '1':
        print(d1.main(inlist))
    elif day == '2':
        print(d2.part1(inlist))
        print(d2.part2(inlist))
    elif day == '3':
        print(d3.part1(inlist))
        print(d3.part2(inlist))
    elif day == '4':
        print(d4.part1(inlist))
    elif day == '5':
        print(d5.main(inlist))
    elif day == '6':
        print(d6.main(inlist))
    elif day == '7':
        print(d7.main(inlist))
    elif day == '8':
        print(d8.main(inlist))
    elif day == '9':
        print(d9.main(inlist))
    elif day == '10':
        print(d10.main(inlist))
    elif day == '11':
        print(d11.main(inlist))
    elif day == '12':
        print(d12.main(inlist))
    elif day == '13':
        print(d13.main(inlist))
    elif day == '14':
        print(d14.main(inlist))
    elif day == '15':
        print(d15.main(inlist))
    elif day == '16':
        print(d16.main(inlist))
    elif day == '17':
        print(d17.main(inlist))
    elif day == '18':
        print(d18.main(inlist))
    elif day == '19':
        print(d19.main(inlist))
    else: raise NotImplementedError()
