preamble = 25
l = [int(x.strip()) for x in open('input').readlines()]
i = 0
invalid = 0
#part 1
for i in range(len(l) - 26):
    found = False
    for j in range(i, 26+i):
        for k in range(i, 26+i):
            if j != k:
                if l[26+i] == l[k] + l[j]:
                    found = True
                    break
        if found:
            break
    if not found:
        invalid = l[i+26]
        print(l[i + 26])
        break
#part 2
i, arr, arrlen = 0, 0, 0
while i < len(l):
    if arr < invalid:
        arr += l[i]
        arrlen += 1
        i += 1
    elif arr == invalid:
        start = i - arrlen
        end = i
        print(min(l[start:end+1]) + max(l[start:end+1]))
        break
    else:
        arr -= l[i - arrlen]
        arrlen -= 1
