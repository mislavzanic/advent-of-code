import fileinput


def modify(rule, rules):
    i = 0
    while i < len(rule):
        c = rule[i]
        if c != '|' and c not in ['a', 'b']:
            c = int(c)
            if rules[c][0][0] == '"':
                rule[i] = rules[c][0][1]
                i += 1
            else:
                if '|' in rules[c]:
                    j = rules[c].index('|')
                    temp = [r for r in rules[c]]
                    rule1 = rule[:i] + temp[:j] + rule[i + 1:]
                    rule1 = modify(rule1, rules)
                    rule2 = rule[:i] + temp[j+1:] + rule[i + 1:]
                    rule2 = modify(rule2, rules)
                    rule = rule1+['|']+rule2
                else:
                    rule = rule[:i]+rules[c]+rule[i+1:]
        else:
            i += 1
    return rule

def part1(rules, strings):
    match = 0
    rule = modify(rules[0], rules)
    rule = ''.join(rule).split('|')
    for s in rule:
        if s in strings:
            match += 1
    return match


def part2(rules, strings):
    rules[8] = ['42', '|', '42', '8']
    rules[11] = ['42', '31', '|', '42', '11', '31']
    rule42 = set(''.join(modify(rules[42], rules)).split('|'))
    rule31 = set(''.join(modify(rules[31], rules)).split('|'))
    len_ = len(list(rule42)[0])

    match = 0
    for s in strings:
        ok = True
        if len(s) % len_ == 0:
            numofstr = len(s) // len_
            n42, n31 = 0, 0
            prev = 0
            for i in range(len_, len(s) + len_, len_):
                if s[prev:i] in rule42:
                    n42 += 1
                    if n31 > 0:
                        ok = False
                        break
                elif s[prev:i] in rule31:
                    n31 += 1
                    if n31 > n42:
                        ok = False
                        break
                else:
                    ok = False
                    break
                prev = i
            if ok:
                if n42 > n31 > 0:
                    match += 1
    return match 

def main():
    lines = [x for x in fileinput.input()]
    rules = {}
    strings = []
    for line in lines:
        x = line.strip()
        if x:
            if x[0] in '1234567890':
                rules[int(x[0:x.index(':')])] = x[x.index(':') + 2:].split()
            else:
                strings.append(x)
    print(part1(rules,strings))
    print(part2(rules, strings))


if __name__ == '__main__':
    main()

