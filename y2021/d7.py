import itertools as it
import re
from collections import defaultdict

def main(inlist):
    inlist = [int(x) for x in inlist[0].split(',')]
    return min(sum(abs(x - y) for x in inlist) for y in inlist), min(sum(abs(x-y)*(abs(x-y) + 1)//2 for x in inlist) for y in inlist)
