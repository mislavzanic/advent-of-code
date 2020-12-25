def pt1(x):
    start = len(x)
    i = 0
    while i < len(x):
        if x.find('(', i) == -1:
            print(start)
            return start
        i = x.find('(', i) + 1
        startlen = i - 1
        a = int(x[i:x.find('x', i)])
        b = int(x[x.find('x', i) + 1:x.find(')', i)])
        i = x.find(')', i)
        start += a * (b - 1)
        start -= i + 1 - startlen
        i += a + 1
    print(start)

def pt2(x):
    i = 0
    start = 0
    if x.find('(') == -1:
        return len(x)

    while i < len(x):

        if x.find('(', i) == -1:
            toAdd = len(x) - i
            return start + toAdd

        new_i = x.find('(', i)
        start += new_i - i
        i = new_i + 1
        nums = x[i: x.find(')', i)]
        a, b = map(int, nums.split('x'))
        i = x.find(')', i) + 1
        toMult = pt2(x[i:i+a]) * b
        start += toMult
        i += a
    return start



x = open('input').readline().strip()
pt1(x)
a = pt2(x)
print(a)
