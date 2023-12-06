from collections import Counter

def main(day):
    pt1 = 0
    pt2 = Counter()
    for i, line in enumerate(day.lines()):
        pt2[i+1] += 1
        nums = [
            [x for x in filter(lambda x: x!='', line.split(" | ")[0].split(": ")[1].split(" "))],
            [x for x in filter(lambda x: x != '', line.split(" | ")[1].split(" "))]
        ]
        winning = [x for x in filter(lambda x: x in nums[0], nums[1])]
        if len(winning) > 0:
            pt1 += pow(2, len(winning) - 1)
        for j, _ in enumerate(winning):
            pt2[i+j+2] += pt2[i+1]

    print(pt1, sum(pt2.values()))
