from typing import List
from functools import reduce

def crt(a: List[int], n: List[int]) -> int:
    p = reduce((lambda x, y: x * y), n)
    return sum(ai * pow(p // ni, -1, ni) * (p // ni) for ai,ni in zip(a,n)) % p
