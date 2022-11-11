import itertools as it
from functools import reduce

def main():
    nums = [int(x.strip()) for x in open("input").readlines()]

    def solve(goal):

        def shortest(nums) -> int:
            for i in range(3, len(nums)):
                if sum(nums[-i:]) < goal: continue
                for item in it.combinations(nums, i):
                    if sum(item) == goal:
                        return i
            return len(nums)

        l = shortest(nums)
        combs = [x for x in it.combinations(nums, l) if sum(x) == goal]
        x = min(combs, key=lambda x: reduce((lambda z, y: z * y), x))
        return reduce((lambda x, y: x * y), x)

    print(solve(sum(nums) // 3))
    print(solve(sum(nums) // 4))


if __name__ == '__main__':
    main()
