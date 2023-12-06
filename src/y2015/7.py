from collections import defaultdict
import re


def checknum(string, lookup):
    if ord(string[0]) < 60:
        return int(string)
    else:
        return lookup[string]


def part2(lines, d):
    new_d = {}
    new_d['b'] = d['a']
    return part1(lines, new_d)


def part1(lines, d):
    while True:
        for line in lines:
            ints = [int(x) for x in re.findall(r'\d+', line)]
            line = line.split()
            dest = line[-1]
            if len(line) == 3:
                if dest in d:
                    continue
                if ints:
                    d[dest] = ints[0]
                elif line[0] in d:
                    d[dest] = d[line[0]]

            elif len(line) == 4:
                num1 = None
                if line[1] in d and not ints:
                    num1 = d[line[1]]
                elif ints:
                    num1 = ints[0]

                if num1 is not None:
                    d[dest] = ~num1

            elif len(line) == 5:
                num1, num2 = None, None
                if line[0] in d:
                    num1 = d[line[0]]
                elif line[0].isdigit():
                    num1 = int(line[0])

                if line[2] in d:
                    num2 = d[line[2]]
                elif line[2].isdigit():
                    num2 = int(line[2])

                if num1 is not None and num2 is not None:
                    if line[1] == 'AND':
                        d[dest] = num1 & num2
                    elif line[1] == 'OR':
                        d[dest] = num1 | num2
                    elif line[1] == 'LSHIFT':
                        d[dest] = num1 << num2
                    else:
                        d[dest] = num1 >> num2

        if 'a' in d:
            return d['a']



def main():
    lines = [x.strip() for x in open('input').readlines()]
    d = {}
    print(part1(lines, d))
    print(part2(lines, d))


if __name__ == '__main__':
    main()
