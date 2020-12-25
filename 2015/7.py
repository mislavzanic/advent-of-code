from collections import defaultdict
l = [x.strip().split() for x in open('i').readlines()]
d = defaultdict(int)
cmds = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']


def checknum(string, lookup):
    if ord(string[0]) < 60:
        return int(string)
    else:
        return lookup[string]

while d['a'] == 0:
    for x in l:
        if len(x) == 3:
            num = checknum(x[0], d)
            wire = x[2]
            d[wire] = num
        elif len(x) == 4:
            num = checknum(x[1], d)
            if num != 0 or ord(x[1][0]) < 60:
                d[x[3]] = ~num
                print(~num)
        elif len(x) == 5:
            num1, num2 = checknum(x[0], d), checknum(x[2], d)
            if x[1] == 'AND':
                d[x[4]] = num1 & num2
            elif x[1] == 'OR':
                if num1 != 0 and num2 != 0:
                    d[x[4]] = num2 | num1
            elif x[1] == 'LSHIFT':
                if num1 != 0 and num2 != 0:
                    d[x[4]] = num1 >> num2
            else:
                if num1 != 0 and num2 != 0:
                    d[x[4]] = num1 << num2

    print(d)
