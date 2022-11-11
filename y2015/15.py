import re
from collections import Counter
from functools import reduce

def parse(l):
    d = {}
    arr = [Counter() for _ in range(len(l))]
    c = Counter()
    for i,line in enumerate(l):
        m = re.match(r'([^:]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',line).groups()
        d[m[0]] = i
        arr[i]['capacity']   = int(m[1])
        arr[i]['durability'] = int(m[2])
        arr[i]['flavor']     = int(m[3])
        arr[i]['texture']    = int(m[4])
        arr[i]['calories']   = int(m[5])
    return d,arr


def main(l):
    d,arr = parse(l)
    m1,m2 = [],[]
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if i + j + k <= 100:
                    temp = [i,j,k,100-i-j-k]
                    cats = ['capacity', 'durability','flavor','texture']
                    p1,p2 = [],[]
                    for c in cats:
                        s,cals = [],[]
                        for key,val in d.items():
                            s.append(temp[val] * arr[val][c])
                            cals.append(temp[val] * arr[val]['calories'])
                        calories = sum(cals)
                        p1.append(sum(s) if sum(s) > 0 else 0)
                        if calories == 500: p2.append(sum(s) if sum(s) > 0 else 0)
                    if p2: m2.append(reduce(lambda x,y: x * y, p2))
                    m1.append(reduce(lambda x,y: x * y, p1))

    print(max(m1),max(m2))


if __name__ == '__main__':
    l = [x.strip() for x in open('15.in').readlines()]
    main(l)
