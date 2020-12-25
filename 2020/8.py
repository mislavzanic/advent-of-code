import sys
from collections import defaultdict

l = [x.strip().split() for x in open('input').readlines()]

def runInstr(instr, ip, acc, changeIndex):
    op, num = instr[0], int(instr[1])
    if op == 'jmp':
        if changeIndex != ip:
            ip += num
        else:
            ip += 1
    elif op == 'nop':
        if changeIndex != ip:
            ip += 1
        else:
            ip += num
    else:
        acc += num
        ip += 1
    return ip, acc

change = []
while True:
    i, acc, index = 0, 0, -1
    d = defaultdict(int)
    zajeb = False
    stack = []
    if change:
        index = change.pop()
    while i < len(l):
        if not change:
            stack.append(i)
        x = l[i]
        d[i] += 1

        if d[i] > 1:
            if not change:
                print(acc)
                while stack:
                    tempindex = stack.pop()
                    if l[tempindex] != 'acc':
                        change.append(tempindex)

            zajeb = True
            break

        i, acc = runInstr(x, i, acc, index)

    if not zajeb:
        break
print(acc)
