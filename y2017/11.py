from collections import defaultdict

x = open('input').readline().strip()
l = x.split(',')
d = defaultdict(int)

m = 0
for x in l:
    d[x] += 1

    if d['n'] < d['s']: 
        d['s'] -= d['n']
        d['n'] = 0
    if d['n'] > d['s']:
        d['n'] -= d['s']
        d['s'] = 0
    if d['nw'] < d['se']: 
        d['se'] -= d['nw']
        d['nw'] = 0
    if d['nw'] > d['se']:
        d['nw'] -= d['se']
        d['se'] = 0
    if d['ne'] < d['sw']: 
        d['sw'] -= d['ne']
        d['ne'] = 0
    if d['ne'] > d['sw']:
        d['ne'] -= d['sw']
        d['sw'] = 0

    if d['n'] > 0:
        if d['sw'] > 0:
            d['sw'] -= 1
            d['n'] -= 1
            d['nw'] += 1
        else:
            d['se'] -= 1
            d['n'] -= 1
            d['ne'] += 1
    elif d['s'] > 0:
        if d['nw'] > 0:
            d['nw'] -= 1
            d['s'] -= 1
            d['sw'] += 1
        else:
            d['ne'] -= 1
            d['s'] -= 1
            d['se'] += 1

    nm = 0
    for v in d.values():
        nm += v
    if nm > m:
        m = nm

print(m)
