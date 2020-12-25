from hashlib import md5

res = ['' for _ in range(8)]

inp = 'ffykfhsq'
i = 0
for j in range(8):
    while True:
        a = inp + str(i)
        tst = md5(a.encode())
        if tst.hexdigest()[:5] == '00000':
            pos = tst.hexdigest()[5]
            if ord(pos) < 60 and int(pos) < 8:
                if res[int(pos)] == '':
                    res[int(pos)] = tst.hexdigest()[6]
                    i += 1
                    break
        i += 1
print(res)
