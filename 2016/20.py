bound = 4294967295
lowest = 0
bounds = []
for x in open('input').readlines():
    x, y = x.strip().split('-')
    x, y = int(x), int(y)
    bounds.append([x, y])

bounds.sort(reverse=False, key=lambda a: a[0])
whitelist = []
for b in bounds:
    if b[0] <= lowest:
        if b[1] >= lowest:
            lowest = b[1] + 1
    else:
        while lowest < b[0]:
            whitelist.append(lowest)
            lowest += 1
        lowest = b[1] + 1
print(whitelist[0], len(whitelist))
