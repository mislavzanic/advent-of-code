from math import sqrt

def main(day):
    parts = []
    for line in day.lines():
        if line.startswith("Time:"):
            time1 = list(map(int, filter(lambda x: x != "", line.split(":")[1].split(" "))))
            time2 = [int("".join(list(filter(lambda x: x != "", line.split(":")[1].split(" ")))))]
            parts.append([time1])
            parts.append([time2])
        if line.startswith("Distance:"):
            dist1 = list(map(int, filter(lambda x: x != "", line.split(":")[1].split(" "))))
            dist2 = [int("".join(list(filter(lambda x: x != "", line.split(":")[1].split(" ")))))]
            parts[0].append(dist1)
            parts[1].append(dist2)

    for part in [1,2]:
        p = 1
        time, dist = parts[part-1]
        for j, _ in enumerate(time):
            bounds = [int((-time[j] - sqrt(pow(time[j], 2) - 4 * dist[j])) // (-2)), int((-time[j] + sqrt(pow(time[j], 2) - 4 * dist[j])) // (-2))]
            p *= (max(bounds) - min(bounds))
        print(p)
