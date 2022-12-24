from math import atan2

def main():
    l = [x.strip() for x in open('input').readlines()]
    d = {}
    for i, row in enumerate(l):
        for j, char in enumerate(row):
            d[(i,j)] = char

    l = []
    coords = {}
    for pos in d.keys():
        coords[pos] = set()
        for k,v in d.items():
            if k == pos: continue
            if v == '.': continue
            coords[pos].add(atan2(pos[0] - k[0], pos[1] - k[1]))
        l.append(len(coords[pos]))
    num = max(l)
    coord = max(coords.keys(), key=lambda k: len(coords[k]))
    print(max(l), coord)
    start = (0, coord[1])

if __name__ == '__main__':
    main()
