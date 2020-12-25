from collections import defaultdict

d = defaultdict(int)
l = [int(x.strip()) for x in open('input').readlines()]
start, end = 0, max(x for x in l) + 3
l.append(end)
l.sort()
# part1
for i in range(len(l)):
    d[l[i] - start] += 1
    start = l[i]
print(d[1] * d[3])

# part2 O(n)
l.append(0)
l.sort()
startpos, i, p = 0, 0, 1
while i < len(l):
    while i < len(l) and l[i] - l[startpos] - 3 <= 0:
        i += 1
    if i < len(l): dif = l[i] - l[startpos] - 3
    else: dif = end - l[startpos] - 3

    if dif == 1:
        p *= ((1<<(i - startpos - 1)) - 1)
    elif dif == 2:
        dif = l[i] - l[i-1]
        if dif == 3:
            p *= (1<<(i-startpos-2))
        elif dif == 2 or dif == 1:
            dif = l[i] - l[i-2]
            if dif < 3:
                p *= ((1<<(i-startpos-1)) - 1)
            else:
                p *= (1<<(i-startpos-2))
    elif dif == 3:
        p *= (1<<(i - startpos - 2))

    if 0 < i < len(l) and l[i] - l[i-1] < 3:
        i -= 1
    startpos = i

print(p)

# part2 dynamic programming
DP = {}
def dp(i):
    if i == len(l) - 1:
        return 1
    if i in DP:
        return DP[i]
    DP[i] = 0
    for j in range(i+1,len(l)):
        if l[j] - l[i] <= 3:
            DP[i] += dp(j)
    return DP[i]
print(dp(0))
