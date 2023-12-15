from aoc_util.advent import Input
from functools import cache

@cache
def dp(springs, blocks, block_size):
    blocks = list(blocks)
    if len(springs) == 0:
        if len(blocks) == 0 and block_size == 0:
            return 1
        if len(blocks) == 1 and block_size == blocks[0]:
            return 1
        return 0
    ans = 0
    if springs[0] in '.?':
        if block_size == 0:
            ans += dp(springs[1:], tuple(blocks), 0)
        if block_size > 0 and blocks != [] and block_size == blocks[0]:
            ans += dp(springs[1:], tuple(blocks[1:]), 0)
    if springs[0] in '#?':
        ans += dp(springs[1:], tuple(blocks), block_size+1)
    return ans

def p2(day: Input):
    s = 0
    for line in day.lines():
        springs, nums = line.split(' ')
        springs = '?'.join([springs for _ in range(5)])
        nums = ','.join([nums for _ in range(5)])
        s += dp(springs, tuple(map(int, nums.split(','))), 0)
    return s

def p1(day: Input):
    s = 0
    for line in day.lines():
        springs, nums = line.split(' ')
        s += dp(springs, tuple(map(int, nums.split(','))), 0)
    return s

