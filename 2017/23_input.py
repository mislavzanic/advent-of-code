from math import sqrt

def prime(n):
    k = int(sqrt(n))
    for i in range(2, k):
        if n % i == 0:
            return 1
    return 0

def primes(lower, higher):
    num = 0
    for i in range(lower, higher, 17):
        num += prime(i)
    return num


b = 93 * 100 + 100000
c = b + 17000
h = 0
h = primes(b, c + 1)
print(b, c)
print(h)



