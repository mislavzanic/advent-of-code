from typing import List
from functools import reduce

def gcd(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return a

def mul_inv(a: int, b: int) -> int:
    if b == 1: return b
    x0,x1,b0 = 0,1,b
    while a > 0:
        x0,x1 = x1 - (a//b)*x0,x0
        a,b = b,a%b
    return x1 if x1 > 0 else x1 + b0

def crt(a: List[int], n: List[int]) -> int:
    p = reduce((lambda x, y: x * y), n)
    return sum(ai * mul_inv((p // ni), ni) * ni for ai,ni in zip(a,n)) % p
