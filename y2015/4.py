from hashlib import md5
import sys

start = 'bgvyzdsv'

i = 254575
while True:
    a = start + str(i)
    res = md5(a.encode())
    res = res.hexdigest()[:6]
    if res == '000000':
        print(i)
        sys.exit(-1)
    i += 1

