from get_input import get_aoc_input


def main():
    with get_aoc_input(6, 2022) as f:
        packets = f.read().strip()
        p1, p2 = False, False
        for i in range(0, len(packets) - 14):

            if p1 and p2: break

            if not p1 and len(set(packets[i:i+4])) == 4:
                print(i + 4)
                p1 = True

            if not p2 and len(set(packets[i:i+14])) == 14:
                print(i + 14)
                p2 = True

if __name__ == '__main__':
    main()
