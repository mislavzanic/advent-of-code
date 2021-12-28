from collections import defaultdict, Counter
import re

def main(l):
    speed = Counter()
    time = Counter()
    rest = Counter()
    resting = Counter()
    running = Counter()
    winning = Counter()
    c = Counter()
    seconds = 2503

    for line in l:
        m = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line).groups()
        speed[m[0]] = int(m[1])
        time[m[0]] = int(m[2])
        rest[m[0]] = int(m[3])
        c[m[0]] = 0

    for i in range(seconds):
        for k in c.keys():
            if running[k] < time[k]:
                c[k] += speed[k]
                running[k] += 1
            else:
                resting[k] += 1
                if resting[k] == rest[k]:
                    resting[k] = 0
                    running[k] = 0
        m = max(c.items(),key=lambda x: x[1])
        for k,v in c.items():
            if v == m[1]: winning[k] += 1
    print(max(c.values()), max(winning.values()))

    

if __name__ == '__main__':
    l = [x.strip() for x in open('input').readlines()]
    main(l)
