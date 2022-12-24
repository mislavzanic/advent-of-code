from collections import defaultdict

def main():
    # n = 7
    n = int(open('input').readline().strip())
    presents = list(i+1 for i in range(n))

    def one_circle(start_pos, presents, length, people):
        gth, lth = 0, 0
        full_circle = False
        curr = start_pos

        while (not full_circle):
            if presents[curr] == 0:
                lth += 1
            else:
                if presents[( curr + (people // 2) + gth - lth ) % length] == 0:
                    assert(False)
                presents[( curr + (people // 2) + gth - lth ) % length] = 0
                gth += 1
                people -= 1

            curr = ( curr + 1 ) % length

            full_circle = curr == 0 or full_circle
            if people == 1:
                break
        return [x for x in presents if x != 0], curr, people

    start_pos, p = 0, n
    while p != 1:
        presents, curr, p = one_circle(start_pos, presents, p, p)
        for i, present in enumerate(presents):
            if present >= curr:
                start_pos = i
                break
    print(presents[0])



    # print(one_circle(0, [i + 1 for i in range(8)], 8, 8), stack)





if __name__ == '__main__':
    main()
