def p2(lines, tokens):
    ll = []
    for line in lines:
        num = ''
        nums = []
        for c in line:
            if c.isnumeric():
                nums.append(c)
                num = ''
            else:
                num += c
                if num in tokens.keys():
                    nums.append(tokens[num])
                    num = c
                if not any(1 if x.startswith(num) else 0 for x in tokens.keys()):
                    if len(num) > 2: num = num[-2:]
                    else: num = c
        ll.append(nums)
    return ll

def main(day):
    l = day.lines()
    tokens = {"one":"1", "two":"2", "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    nums = [[x for x in line if x.isnumeric()] for line in l]
    print(sum(int(x[0]+x[-1]) for x in nums if x != [])) 
    nums = [[x for x in line if x.isnumeric()] for line in p2(l, tokens)]
    print(sum(int(x[0]+x[-1]) for x in nums)) 
