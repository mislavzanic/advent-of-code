from aoc_util.advent import Input

def reflection(matrix):
    h, v = [], []
    for i,_ in enumerate(matrix):
        length = min(i, len(matrix) - i)
        horizontal = []
        for ii in range(length):
            for j,c in enumerate(matrix[ii+i]):
                horizontal.append(c == matrix[i - ii - 1][j])
        if all(horizontal) and horizontal:
            assert i != 0
            h.append(100 * i)

    for j in range(len(matrix[0])):
        length = min(j, len(matrix[0]) - j)
        vertical = []
        for jj in range(length):
            for i in range(len(matrix)):
                vertical.append(matrix[i][j+jj] == matrix[i][j-jj-1])
        if all(vertical) and vertical:
            assert j != 0
            v.append(j)
    return h + v

def p2(day:Input):
    matrices = map(lambda s: s.split('\n'), day.string().split('\n\n'))
    s = 0
    for matrix in matrices:
        num = 0
        old_reflection = sum(reflection(list(filter(lambda x: x!='', matrix))))
        for i,line in enumerate(matrix):
            for j,c in enumerate(line):
                new_c = '.' if c != '.' else '#'
                new_matrix = [
                    [
                        new_c if j == jj else cc
                          for jj,cc in enumerate(line)
                    ] if i == ii else line
                    for ii,line in enumerate(matrix)
                ] 
                r = reflection(list(filter(lambda x: x!='', new_matrix)))
                if list(filter(lambda x: x != 0 and x != old_reflection, r)):
                    num = list(filter(lambda x: x != 0 and x != old_reflection, r))[0]
                    break
            if num != 0 and num != old_reflection:
                break
        assert num != 0 and num != old_reflection, f'{num}'
        s += num
    return s

def p1(day: Input):
    matrices = map(lambda s: s.split('\n'), day.string().split('\n\n'))
    s = 0
    for matrix in matrices:
        s += sum(reflection(list(filter(lambda x: x!='', matrix))))
    
    return s


