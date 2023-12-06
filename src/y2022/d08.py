from get_input import get_aoc_input

import itertools as it

def main():
    l = []
    with get_aoc_input(8, 2022) as f:
        l = [x.strip() for x in f.readlines()]
    p1, p2 = [], []

    for i, row in enumerate(l):
        for j, tree in enumerate(row):
            predicate = lambda x: int(x) < int(tree)
            m = [
                len(list(it.takewhile(predicate, [l[i][k] for k in reversed(range(0, j))]))),
                len(list(it.takewhile(predicate, [l[i][k] for k in range(j + 1, len(row))]))),
                len(list(it.takewhile(predicate, [l[k][j] for k in reversed(range(0, i))]))),
                len(list(it.takewhile(predicate, [l[k][j] for k in range(i + 1, len(l))])))
            ]
            m[0] += int(m[0] != j)
            m[1] += int(m[1] != len(row) - j - 1)
            m[2] += int(m[2] != i)
            m[3] += int(m[3] != len(l) - i - 1)

            p2.append(m[0] * m[1] * m[2] * m[3])
            p1.append(int(any([
                i == 0 or i == len(l) - 1,
                j == 0 or j == len(row) - 1,
                all(int(other) < int(tree) for k, other in enumerate(l[i]) if k < j),
                all(int(other) < int(tree) for k, other in enumerate(l[i]) if k > j),
                all(int(tree) > int(l[k][j]) for k in range(0, i)),
                all(int(tree) > int(l[k][j]) for k in range(i+1, len(l)))
            ])))
    print(sum(p1), max(p2))


if __name__ == '__main__':
    main()
