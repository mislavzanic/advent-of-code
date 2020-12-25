from collections import defaultdict

s = 0
for x in open('input').readlines():
    x = x.strip().split('-')
    l = x[-1][x[-1].find('[') + 1:x[-1].find(']')]
    num = int(x[-1][:x[-1].find('[')])
    x = x[:-1]
    nums = defaultdict(int)

    for w in x:
        for c in w:
            nums[c] += 1
    roomvals = []
    for c in l:
        roomvals.append(nums[c])
    vals = list(nums.values())
    vals.sort(reverse=True)
    decoy = False
    for i in range(5):
        if vals[i] != roomvals[i]:
            decoy = True
            break

        if i < len(roomvals) - 1:
            if roomvals[i] == roomvals[i + 1]:
                if l[i] > l[i + 1]:
                    decoy = True
                    break
 
    if not decoy:
        real = []

        for w in x:
            for c in w:
                temp = num
                new = ord(c)
                while temp > 0:
                    new += 1
                    if new > ord('z'):
                        new = ord('a')
                    temp -= 1
                real.append(chr(new))
            real.append(' ')

        print(''.join(real), num)
        s += num
print(s)
