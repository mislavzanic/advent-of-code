l = [x.strip() for x in open('input').readlines()]

sets = []
a, b, j = 0, 0, 0
for x in l:
    x = x.split()
    if x:
        sets.append(set())
        for i in range(len(x)):
            c = x[i]
            for cc in c:
                sets[j].add(cc)
        j += 1
    else:
        anyone, all_ = sets[0].copy(), sets[0].copy()
        for i in range(len(sets) - 1):
            anyone = anyone.union(sets[i+1])
            all_ = all_.intersection(sets[i+1])
        b += len(anyone)
        a += len(all_)
        j, sets = 0, []

anyone, all_ = sets[0].copy(), sets[0].copy()
for i in range(len(sets) - 1):
    anyone = anyone.union(sets[i+1])
    all_ = all_.intersection(sets[i+1])
b += len(anyone)
a += len(all_)

print(b)
print(a)
