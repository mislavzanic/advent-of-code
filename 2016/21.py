from collections import deque
import itertools

def scramble(string, instr):
    q = [c for c in string]
    for x in instr:
        if x[0] == 'swap':
            if x[1] == 'position':
                i, j = int(x[2]), int(x[-1])
                q[i], q[j] = q[j], q[i]
            else:
                i, j = q.index(x[2]), q.index(x[-1])
                q[i], q[j] = q[j], q[i]
        elif x[0] == 'reverse':
            i, j = int(x[2]), int(x[-1])
            temp = q[i:j+1]
            temp.reverse()
            q = q[:i] + temp + q[j+1:]
        elif x[0] == 'rotate':
            if x[1] == 'left':
                q = deque(q)
                q.rotate(-int(x[2]))
            elif x[1] == 'right':
                q = deque(q)
                q.rotate(int(x[2]))
            else:
                letter = x[-1]
                i = q.index(letter)
                q = deque(q)
                if i >= 4:
                    q.rotate(i + 2)
                else:
                    q.rotate(i + 1)
            q = list(q)
        else:
            element = q[int(x[2])]
            q.remove(element)
            q.insert(int(x[-1]), element)
    return ''.join(q)


instr = []
for x in open('input').readlines():
    x = x.strip().split()
    instr.append(x)
print(scramble('abcdefgh', instr))
goal = 'fbgdceah'
for p in itertools.permutations('abcdefgh'):
    if scramble(p, instr) == goal:
        print(''.join(p))
