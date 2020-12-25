l = [x for x in open('input').readline()]
l = l[:len(l) - 1]

def checkNeg(l, index, neg):
    while index < len(l) and l[index] == '!':
        index += 1
        neg = not neg
    return index, neg

i = 0
group = 0
score = 0
trash = False
count = 0
while i < len(l) - 1:
    newindex = 0
    neg = False
    newindex, neg = checkNeg(l, i, neg)
    if neg:
        i = newindex + 1
        continue
    else:   
        i = newindex

    if l[i] == '<' and not trash:
        trash = True
    elif l[i] == '>' and trash:
        trash = False
    elif trash:
        count += 1
        i += 1
        continue
    elif l[i] == '{' and not trash:
        group += 1
        score += group
    elif l[i] == '}' and not trash:
        group -= 1
        
    elif l[i] == '<' and not trash:
        trash = True
    elif l[i] == '>' and trash:
        trash = False
    elif trash:
        i += 1
        continue

    if newindex - i == 0:
        i += 1
    else:
        i = newindex

print(score, count)




