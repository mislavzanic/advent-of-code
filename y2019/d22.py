#!/usr/bin/env python3


def cut(N, card_pos, num_of_cards):
    return (card_pos - N) % num_of_cards

def deal_with_increment(N, card_pos, num_of_cards):
    return (card_pos * N) % num_of_cards

def deal_new_stack(card_pos, num_of_cards):
    return num_of_cards - 1 - card_pos


def main():
    shuffle = [x.strip() for x in open('input').readlines()]

    def shuffle_cards(card_pos, num_of_cards):
        a, b = 1, 0
        for s in shuffle:
            if s == "deal into new stack":
                card_pos = deal_new_stack(card_pos, num_of_cards)
                a *= -1
                b = num_of_cards - 1 - b
                continue

            N = int(s.split(" ")[-1])

            if s.split(" ")[0] == "cut":
                card_pos = cut(N, card_pos, num_of_cards)
                b -= N
                continue

            if s.split(" ")[0] == "deal":
                card_pos = deal_with_increment(N, card_pos, num_of_cards)
                a *= N
                b *= N
                continue

            assert(False)
        return card_pos, a % num_of_cards, b % num_of_cards

    def big_shuffle(start):
        num_of_cards, times = 119315717514047, 101741582076661
        _, c, d = shuffle_cards(start, num_of_cards)
        a, b = pow(c, -1, num_of_cards), (-d * pow(c, -1, num_of_cards)) % num_of_cards
        p1 = pow(a, times, num_of_cards)
        p2 = (p1 - 1) * pow(a - 1, num_of_cards - 2, num_of_cards)
        return (( p1 * start ) + ( b * p2 )) % num_of_cards


    print(shuffle_cards(2019, 10007)[0])
    print(big_shuffle(2020))



if __name__ == '__main__':
    main()
