import sys

path = []

for x in open('input').readlines():
    if x[-1] == '\n':
        x = x[:-1]
    path.append(x)


startj = path[0].find('|')
start = (0, startj)
DIR = 1 # 0 up, 1 down, 2 left, 3 right
keys = list()
step = 0

while True:
    i, j = start[0], start[1]
    assert path[i][j] != ' '
    if path[i][j] == '+':
        if DIR == 1 or DIR == 0:
            if j > 0:
                if path[i][j - 1] == '-':
                    DIR = 2
            if j < len(path[i]) - 1:
                if path[i][j + 1] == '-':
                    DIR = 3
        else:
            if i > 0:
                if path[i - 1][j] == '|':
                    DIR = 0
            if i < len(path) - 1:
                if path[i + 1][j] == '|':
                    DIR = 1

    elif path[i][j] not in [' ', '|', '-', '+']:
        assert path[i][j] != ' '
        keys.append(path[i][j])
        if path[i][j] == 'O':
            print(''.join(keys))
            print(step + 1)
            sys.exit(-1)
    if DIR == 0:
        i -= 1
    elif DIR == 1:
        i += 1
    elif DIR == 2:
        j -= 1
    else:
        j += 1
    step += 1
    start = (i, j)
