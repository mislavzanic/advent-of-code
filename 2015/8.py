import fileinput


def part1(lines):
    C, M = 0, 0
    for line in lines:
        code, memory = 2, 0
        line = line[1:-1]
        num = len(line)
        code, memory = code + num, memory + num
        i = 0
        while i < len(line):
            c = line[i]
            if c == '\\':
                if line[i + 1] == 'x':
                    memory -= 3
                    i += 3
                elif line[i + 1] == '\\' or line[i + 1] == '\"':
                    memory -= 1
                    i += 1
            i += 1
        C, M = C + code, M + memory
    return C - M



def part2(lines):
    new_lines = []
    for line in lines:
        new_line = '\"'
        for i, c in enumerate(line):
            if c == '\\':
                new_line += '\\\\'
            elif c == '\"':
                new_line += '\\\"'
        new_line += '\"'
        new_lines.append(new_line)
    return part1(new_lines)


def main():
    lines = [x.strip() for x in fileinput.input()]
    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
