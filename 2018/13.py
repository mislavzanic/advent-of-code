from collections import defaultdict

l = [x[:-1] for x in open('input').readlines()]
cross = []
start = {'<':3, '>':1, 'v':2, '^':0}
carts = defaultdict(list)
for i in range(len(l)):
    l[i] = [c for c in l[i]]
    for j in range(len(l[i])):
        if l[i][j] == '+':
            cross.append([i, j])
        elif l[i][j] in start.keys():
            carts[(i, j)] = [start[l[i][j]], 0]
            l[i][j] = '|' if  l[i][j] == 'v' or l[i][j] == '^' else '-'

while True:
    for k, v in carts.items():
        i, j = k
        if 0 <= i <= len(l):
            if 0 <= j <= len(l[i]):
                cart_dir, cart_turn = v
                if l[i][j] == '+':
                    if cart_turn == 0:
                        carts[k][0] -= 1
                        carts[k][0] %= 4
                    elif cart_turn == 2:
                        carts[k][0] += 1
                        carts[k][0] %= 4
                    carts[k][1] += 1
                    carts[k][1] %= 3
                elif l[i][j] == '/':



