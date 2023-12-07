from collections import defaultdict

def srt(hand, order):
    return sum([order.index(c) * (pow(len(order), len(hand) - i - 1)) for i, c in enumerate(hand)])

def p1(day):
    order = '0123456789TJQKA'
    bids = defaultdict(int)
    hands = defaultdict(lambda: defaultdict(int))
    for line in day.lines():
        hand, bid = line.split()[0], line.split()[1]
        bids[hand] = int(bid)
        for c in hand:
            hands[hand][c] += 1
    return sort_hands(bids, hands, order)

def p2(day):
    order = '01J23456789TQKA'
    bids = defaultdict(int)
    hands = defaultdict(lambda: defaultdict(int))
    for line in day.lines():
        hand, bid = line.split()[0], line.split()[1]
        bids[hand] = int(bid)
        for c in hand:
            hands[hand][c] += 1
        if "J" in hand:
            l = [(k,v) for k,v in hands[hand].items() if k != "J"]
            if l != []:
                k,_ = max(l, key=lambda p: p[1])
                hands[hand][k] += hands[hand]["J"]
                del hands[hand]["J"]
    return sort_hands(bids, hands, order)

def sort_hands(bids, hands, order):
    all_hands = [y for x in map(lambda x: sorted(x, key=lambda y: srt(y, order), reverse=True), [
      [x for x in hands.keys() if all(v == 5 for v in hands[x].values())],
      [x for x in hands.keys() if any(v == 4 for v in hands[x].values())],
      [x for x in hands.keys() if all(2 <= v <= 3 for v in hands[x].values())],
      [x for x in hands.keys() if all(v in [1,3] for v in hands[x].values()) and any(v == 3 for v in hands[x].values())],
      [x for x in hands.keys() if len([v for v in hands[x].values() if v == 2]) == 2],
      [x for x in hands.keys() if len([v for v in hands[x].values() if v == 2]) == 1 and all([1 <= v <= 2 for v in hands[x].values()])],
      [x for x in hands.keys() if all(v == 1 for v in hands[x].values())],
    ]) for y in x]
    return sum((len(all_hands) - i) * bids[c] for i,c in enumerate(all_hands))
    

