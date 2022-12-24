def p2(lines, tokens):
    ll = []
    for line in lines:
        min_ind = {}
        max_ind = {}
        for k in tokens.keys():
            m, M = line.find(k), line.rfind(k)
            if m == -1: continue
            min_ind[m] = k
            max_ind[M] = k
            
            if len(min_ind) > 0:
                m, M = min(min_ind.keys()), max(max_ind.keys())
                if not any(1 if x in line[:m] else 0 for x in "123456789"):
                    line = tokens[min_ind[m]].join(line.split(min_ind[m], 1))
                    if line.rfind(max_ind[M]) > -1 and not any(1 if x in line[M:] else 0 for x in "123456789"):
                        line = tokens[max_ind[M]].join(line.rsplit(max_ind[M], 1))
                        ll.append(line)
                        
    return ll

def main():
    l = [x.strip() for x in open('1.input').readlines()]
    tokens = {"one":"1", "two":"2", "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    nums = [[x for x in line if x.isnumeric()] for line in l]
    print(sum(int(x[0]+x[-1]) for x in nums)) 
    nums = [[x for x in line if x.isnumeric()] for line in p2(l, tokens)]
    print(sum(int(x[0]+x[-1]) for x in nums)) 

if __name__ == '__main__':
    main()

