p1 = [4, 2, 4, 0]
p2 = [8, 2, 4, 0]

num = 0
for i in range(len(p1) - 1):
    p1[i + 1] += p1[i]
    num += (p1[i] - 1) * 2 - 1
print(num)
num = 0
for i in range(len(p1) - 1):
    p2[i + 1] += p2[i]
    num += (p2[i] - 1) * 2 - 1
print(num)
