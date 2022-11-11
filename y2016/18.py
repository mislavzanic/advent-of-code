inp = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
safe = 0
for i in range(400000):
    for c in inp:
        safe += c=='.'
    newinput = ''
    j = 0
    while len(newinput) < len(inp):
        if j == 0:
            if inp[0] == '^' and inp[1] == '^':
                newinput += '^'
            elif inp[0] == '.' and inp[1] == '^':
                newinput += '^'
            else:
                newinput += '.'
        elif j == len(inp) - 1:
            if inp[-1] == '^' and inp[-2] == '^':
                newinput += '^'
            elif inp[-1] == '.' and inp[-2] == '^':
                newinput += '^'
            else:
                newinput += '.'
        else:
            if inp[j - 1] == inp[j] == '^' and inp[j + 1] == '.':
                newinput += '^'
            elif inp[j + 1] == inp[j] == '^' and inp[j - 1] == '.':
                newinput += '^'
            elif inp[j + 1] == inp[j] == '.' and inp[j - 1] == '^':
                newinput += '^'
            elif inp[j - 1] == inp[j] == '.' and inp[j + 1] == '^':
                newinput += '^'
            else:
                newinput += '.'

        j += 1
    inp = newinput
print(safe)
