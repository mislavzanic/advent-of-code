import fileinput
import re
from functools import reduce

def mod_inv(a,b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a>1:
        q=a//b
        a,b=b,a%b
        x0,x1=x1-(q*x0),x0
    if x1<0: x1+=b0
    return x1


def crt(primes,mods):
    S = 0
    P = reduce(lambda a,b:a*b, primes)
    for pi, mi in zip(primes,mods):
        rp = P/pi
        S += mi*mod_inv(rp,pi)*rp
    return S%P

def p1(bus, times):
    mods = []
    for t in times:
        mods.append(t-bus%t)
    m = min(mods)
    index = mods.index(m)
    return m*times[index]


def p2(time):
    primes, mods = [], []
    for i,t in enumerate(time):
        if t != 0:
            primes.append(t)
            if i == 0:
                mods.append(t)
            else:
                mods.append((t-i)%t)
    return crt(primes,mods)

lines = [x for x in list(fileinput.input())]

bus = 0
t = []
for line in lines:
    ints = re.findall('\d+', line)
    if len(ints) == 1:
        bus = int(ints[0])
    else:
        l = line.split(',')
        for i in l:
            if i != 'x':
                t.append(int(i.strip()))
            else:
                t.append(0)
print(p1(bus, [int(i) for i in ints]))
print(p2(t))
