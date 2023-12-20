from functools import reduce
from aoc_util.advent import Input

def parse(day: Input):
    wfl, rules = day.string().strip().split('\n\n')
    wfl = wfl.split('\n')
    r = {}
    for line in wfl:
        name, rule = line.split('{')
        rule = rule[:-1].split(',')
        r[name] = rule
    data = []
    for rule in rules.split('\n'):
        data.append({a:b for (a,b) in map(lambda x: (x.split('=')[0], int(x.split('=')[1])),rule[1:-1].split(','))})
    return r, data

def sort(data, rules):
    curr = 'in'
    while curr not in 'AR':
       rule = rules[curr]
       for item in rule:
           if ':' in item:
               cond, goto = item.split(':')
               if '>' in cond:
                   f, n = cond.split('>')
                   n = int(n)
                   if data[f] > n:
                       curr = goto
                       break
               else:
                   f, n = cond.split('<')
                   n = int(n)
                   if data[f] < n:
                       curr = goto
                       break
           else:
               curr = item
               break
    if curr == 'A':
        return sum(data.values())
    return None

def traverse(rules, curr):
    def negate(cond):
        return cond.split('>')[0] + '<' + str(int(cond.split('>')[1]) + 1) if '>' in cond else cond.split('<')[0] + '>' + str(int(cond.split('<')[1]) - 1)

    paths = []
    neg_rules = []
    for rule in rules[curr]:
        if ':' not in rule:
            if rule in 'AR':
                return paths + [neg_rules + [rule]]

            child_paths = traverse(rules, rule)
            for cp in child_paths: paths.append(neg_rules + cp)
            return paths

        cond, goto = rule.split(':')
        if goto in 'AR':
            paths.append(neg_rules + [cond, goto])
        else:
            child_paths = traverse(rules, goto)
            for cp in child_paths: paths.append(neg_rules + [cond] + cp)
        neg_rules.append(negate(rule.split(':')[0]))
    return paths

def p2(day: Input):
    rules, _ = parse(day)
    paths = traverse(rules, 'in')
    variables = []
    for path in paths:
        if path[-1] == 'R': continue
        variables.append({})
        path = path[:-1]
        lt, gt = {}, {}
        for cond in path:
            if '>' in cond:
                var, num = cond.split('>')
                num = int(num)
                if var in gt:
                    gt[var] = num if num > gt[var] else gt[var]
                else:
                    gt[var] = num
            else:
                var, num = cond.split('<')
                num = int(num)
                if var in lt:
                    lt[var] = num if num < lt[var] else lt[var]
                else:
                    lt[var] = num
        for c in 'xmas':
            nums = 4000
            if c in gt: nums = nums - gt[c]
            if c in lt: nums = nums - (4000 - lt[c] + 1)
            variables[-1][c] = nums

    return sum(reduce(lambda x, y: x * y, x.values()) for x in variables)

def p1(day: Input):
    rules, data = parse(day)
    s = 0
    for d in data:
        r = sort(d, rules)
        if r != None: s += r
    return s
        
