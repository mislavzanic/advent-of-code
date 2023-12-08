from math import sqrt

def p1(day):
    time, dist = [], []
    for line in day.lines():
        if line.startswith("Time:"):
            time = list(map(int, filter(lambda x: x != "", line.split(":")[1].split(" "))))
        if line.startswith("Distance:"):
            dist = list(map(int, filter(lambda x: x != "", line.split(":")[1].split(" "))))
    return solve(time, dist)

def p2(day):
    time, dist = [], []
    for line in day.lines():
        if line.startswith("Time:"):
            time = [int("".join(list(filter(lambda x: x != "", line.split(":")[1].split(" ")))))]
        if line.startswith("Distance:"):
            dist = [int("".join(list(filter(lambda x: x != "", line.split(":")[1].split(" ")))))]
    return solve(time, dist)

def solve(time, dist):
    p = 1
    for d, t in zip(dist, time):
        bounds = [int((-t - sqrt(pow(t, 2) - 4 * d)) // (-2)), int((-t + sqrt(pow(t, 2) - 4 * d)) // (-2))]
        p *= (max(bounds) - min(bounds))
    return p
    
