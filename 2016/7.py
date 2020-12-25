def check(string):
    j = 0
    while j < len(string) - 3:
        if (string[j] == string[j + 3] and string[j + 1] == string[j + 2] and string[j + 1] != string[j]):
            return True
        j += 1
    return False

def check2(string, S):
    j = 0
    while j < len(string) - 2:
        if (string[j] == string[j + 2] and string[j + 1] != string[j]):
            S.add(string[j:j+3])
        j += 1
    return S

p1 = 0
p2 = 0
for x in open('input').readlines():
    x = x.strip()
    i = 0
    foundABBA = False
    foundNONABBA = False
    ABA = set()
    BAB = set()
    while i < len(x):
        abbaStr = ''
        nonabbaStr = ''
        while i < len(x) and x[i] != '[':
            abbaStr += x[i]
            i += 1
        i += 1
        while i < len(x) and x[i] != ']':
            nonabbaStr += x[i]
            i += 1
        i += 1
        if not foundABBA:
            foundABBA = check(abbaStr)
        if not foundNONABBA:
            foundNONABBA = check(nonabbaStr)
        ABA = check2(abbaStr, ABA)
        BAB = check2(nonabbaStr, BAB)
    if not foundNONABBA:
        if foundABBA:
            p1 += 1
   
    found = False
    for aba in ABA:
        for bab in BAB:
            if aba[0] == bab[1] and bab[0] == aba[1]:
                p2 += 1
                found = True
                break
        if found: break


print(p1, p2)
