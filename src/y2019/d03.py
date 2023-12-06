def main():
    l = [x.strip().split(',') for x in open('input').readlines()]
    d = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}

    p, q = [], []
    def path(wire, s):
        start = (0,0)
        for item in wire:
            direction, dist = item[0], int(item[1:])
            for _ in range(dist):
                start = (start[0] + d[direction][0], start[1] + d[direction][1])
                s.append(start)
        return s

    p = path(l[0],p)
    q = path(l[1],q)
    intersection = set(p) & set(q)

    print(abs(sum(min(intersection, key=lambda point: abs(point[0]) + abs(point[1])))))
    print(min(len(p[:p.index(point) + 1]) + len(q[:q.index(point) + 1]) for point in intersection))


if __name__ == '__main__':
    main()
