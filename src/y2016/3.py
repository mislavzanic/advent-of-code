num = 0
for x in open('input').readlines():
    x = x.strip()
    x = x.split()
    x = [int(c) for c in x]
    if x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[2] + x[0] > x[1]:
        num += 1
print(num)

triangles = []
for x in open('input').readlines():
    x = x.strip().split()
    x = [int(c) for c in x]
    triangles.append(x)

index = 0
num = 0
while index < len(triangles):
    temp = []
    for i in range(3):
        temptemp = []
        for j in range(3):
            temptemp.append(triangles[index + j][i])
        temp.append(temptemp)
    for x in temp:
        if x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[2] + x[0] > x[1]:
            num += 1
    index += 3
print(num)
