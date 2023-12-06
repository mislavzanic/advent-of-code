from collections import defaultdict

d = defaultdict(set)

ports = []

for x in open('input').readlines():
    x = x.strip()

    a, b = int(x[:x.find('/')]), int(x[x.find('/') + 1:])
    if b < a:
        a, b = b, a
    ports.append((a,b))

