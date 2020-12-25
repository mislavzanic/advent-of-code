from collections import defaultdict
from collections import deque
import sys

def program(ID, d, i, q, instructions, cnt, deadlock):
    while i[ID] < (len(instructions)):
        (cmd, x, y) = instructions[i[ID]]
        if y != '':
            if isinstance(y, str):
                if len(y) == 1 and ord(y) > 60:
                    y = d[ID][y]
                else:
                    y = int(y)
        if ord(x) < 60:
            i[ID] += 3
            continue

        if cmd == 'set':
            d[ID][x] = y
        elif cmd == 'add':
            d[ID][x] += y
        elif cmd == 'mul':
            d[ID][x] *= y
        elif cmd == 'mod':
            d[ID][x] %= y
        elif cmd == 'jgz':
            if d[ID][x] > 0:
                i[ID] += y
                continue 

        elif cmd == 'rcv':
            if q[ID]:
                d[ID][x] = q[ID][0]
                q[ID].popleft()

            else:
                if deadlock:
                    print(cnt)
                    sys.exit(-1)

                deadlock = True if len(q[(ID + 1) % 2]) > 0 else False

                if ID == 0:
                    return 1, d, i, q, instructions, cnt, deadlock
                else:
                    ID, d, i, q, instructions, cnt, deadlock = program(0, d, i, q, instructions, cnt, deadlock)
                    continue

        elif cmd == 'snd':
            deadlock = False
            q[(ID + 1) % 2].append(d[ID][x]) 
            if ID == 1:
                cnt += 1

        if i[ID] < 0 or i[ID] >= len(instructions):
            break

        i[ID] += 1

    return (ID + 1) % 2, d, i, q, instructions, cnt, deadlock

d = [defaultdict(int), defaultdict(int)]
index = [0, 0]
instructions = list()
cnt = 0
q = [deque(), deque()]
for instr in open('input').readlines():
    instr = instr.strip()
    cmd,x,y = instr[:3], instr[4], instr[6:]
    instructions.append((cmd, x, y))
d[1]['p'] = 1
d[0]['p'] = 0
deadlock = False
ID = 1
while not deadlock:
    ID, d, i, q, instructions, cnt, deadlock = program(ID, d, index, q, instructions, cnt, False)
    if deadlock:
        print(cnt)
        break

