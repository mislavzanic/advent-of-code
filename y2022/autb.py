from typing import List
from functools import reduce

def gcd(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return a

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
# A Python3 program to demonstrate
# working of Chinese remainder
# Theorem

# Returns modulo inverse of a with
# respect to m using extended
# Euclid Algorithm. Refer below
# post for details:
# https://www.geeksforgeeks.org/
# multiplicative-inverse-under-modulo-m/
def inv(a, m) :

    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1) :
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1) :
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

    # Make x1 positive
    if (x1 < 0) :
        x1 = x1 + m0

    return x1

# k is size of num[] and rem[].
# Returns the smallest
# number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime
# (gcd for every pair is 1)

def crt(a: List[int], n: List[int]) -> int:
	p = reduce((lambda x, y: x * y), n)
	return sum(ai * inv((p // ni), ni) * (p // ni) for ai,ni in zip(a,n)) % p
	# return sum(ai * pow(ni, -1, p//ni) * (p//ni) for ai,ni in zip(a,n)) % p
