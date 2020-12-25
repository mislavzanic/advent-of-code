L = [int(x.strip()) for x in open('input').readlines()]

p1 = 0
p2 = 0
for i in range(len(L) - 1):
    for j in range(i, len(L)):
        if L[i] + L[j] == 2020:
            p1 = L[i] * L[j]
        for k in range(j, len(L)):
            if L[i] + L[j] + L[k] == 2020:
                p2 = L[i] * L[j] * L[k]
print(p1,p2)
    
    
