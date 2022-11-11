import os
import re
from collections import defaultdict
import itertools as it
import random
import sys

def main():
    result = '''C(CaSi(BSi(F)TiBPTiTiBF)PBCaSiThSi(TiBPBPMg)CaSi(TiMg)CaSiThCaSi(F)(Si(F)TiTiBF)CaCaSi(SiThCaCaSi(Mg)F,Si(F,CaF)SiThCaSiThPBPTiMg)CaP(SiAl)PBCaCaSi(F,SiThCa(F))CaCaSi(PBSi(F)Mg,CaCaCaCaSiThCaCaSiAl)CaCaSi(PBSiAl)BCaCaCaCaSiThCaPBSiThPBPBCaSi(F,F)SiThCaSi(F)BCaCaSi(F,F)SiThCaPBSiThCaSi(PMg)(F)PTiBCaP(F)CaCaCaCaSi(CaCaSi(F,F)F)BCaSiThF)ThSiThSi(Ti(PMg)F)CaSiThCaPBCaSi(BF)CaCaP(CaCaPMg)Si(F,F)CaSiTh(PBPMg)'''
    rules = '''Al => ThF
    Al => Th(F)
    B => BCa
    B => TiB
    B => Ti(F)
    Ca => CaCa
    Ca => PB
    Ca => P(F)
    Ca => Si(F,F)
    Ca => Si(Mg)
    Ca => SiTh
    F => CaF
    F => PMg
    F => SiAl
    H => C(Al)
    H => C(F,F,F)
    H => C(F,Mg)
    H => C(Mg,F)
    H => HCa
    H => N(F,F)
    H => N(Mg)
    H => NTh
    H => OB
    H => O(F)
    Mg => BF
    Mg => TiMg
    N => C(F)
    N => HSi
    O => C(F,F)
    O => C(Mg)
    O => HP
    O => N(F)
    O => OTi
    P => CaP
    P => PTi
    P => Si(F)
    Si => CaSi
    Th => ThCa
    Ti => BP
    Ti => TiTi
    e => HF
    e => NAl
    e => OMg'''

    d = parse(rules)
    keys = list(d.keys())
    keys.sort(key=lambda x: len(x), reverse=True)

    minimum = 10000

    # def solve(r: str):
    #     step = 0
    #     while r != 'e':
    #         seen = False
    #         for key in keys:
    #             pos = r.find(key)
    #             if pos != -1:
    #                 r = r[:pos] + d[key][0] + r[pos + len(key):]
    #                 seen = True
    #                 step += 1
    #                 break
    #         if not seen:
    #             print(r)
    #             break
    #     return step

    def recurse(r, m, step):
        while r != 'e':
            seen = False
            for key in keys:
                pos = r.find(key)
                if pos != -1:
                    if r == "e":
                        print(step)
                        sys.exit(1)
                    found, steps = recurse(r[:pos] + d[key][0] + r[pos + len(key):], m, step + 1)
                    if found:
                        seen = True
                        if steps < m: m = steps
                        if minimum > m: print("new min: " + str(m))
                        sys.exit(1)
            if not seen:
                # print(r, step)
                return False, -1
        if step < m: m = step
        print(m)
        return True, m

    recurse(result, minimum, 0)

def parse(rules: str):
    d = defaultdict(list)
    r = rules.split('\n')
    for rule in r:
        a  = re.findall('([a-zA-Z]+) => ([a-zA-Z]+)', rule)[0]
        d[a[1]].append(a[0])
    return d

if __name__ == '__main__':
    main()
