import fileinput
import re

lines = [x.strip() for x in fileinput.input()]
l = []
for line in lines:
    ints = [int(x) for x in re.findall('-?\d+',line)]
    l.append(ints[0])

val = 1
div = 20201227
subject = 7
lsizes = []
for i in range(2):
    key = l[i]
    loopsize = 0
    val = 1
    while True:
        val = val * subject
        val = val % div

        if val == key:
            break
        loopsize += 1
    lsizes.append(loopsize + 1)
print(lsizes)   
for i in range(2):
    val = 1
    while lsizes[1-i]:
        val *= l[i] 
        val %= div
        lsizes[1-i] -= 1
    print(val)
