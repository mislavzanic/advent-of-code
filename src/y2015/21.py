#!/usr/bin/env python3


shop = '''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class Item:
    def __init__(self, c, d, a):
        self.cost = c
        self.damage = d
        self.armor = a

    # def __eq__(self, other):
    #     return self.cost == other.cost and self.damage == other.damage and self.armor == other.armor

    def __lt__(self, other):
        return self.cost < other.cost or ( self.cost == other.cost and ( self.damage < other.damage or (self.damage == other.damage and self.armor < other.armor ) ) )

    def __str__(self):
        return str(self.cost) + "," + str(self.armor) + "," + str(self.damage)

wepons = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(75, 8, 0)
]

armor = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5)
]

rings = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3)
]

class Ent:
    def __init__(self, hp, d, a, items):
        self.hp = hp
        self.damage = d
        self.armor = a
        self.items = items

    def attack(self, other):
        if self.hp <= 0: return

        d,a = self.damage,other.armor

        for item in self.items:
            d += item.damage

        for item in other.items:
            a += item.armor

        d = d - a if d > a else 1

        other.hp -= d

def simulate(player):
    boss = Ent(109, 8, 2, [])

    while True:
        player.attack(boss)
        boss.attack(player)

        if boss.hp <= 0: return True
        if player.hp <= 0: return False

def acceptable(items):
    if len(set(wepons) & set(items)) != 1: return False
    if len(set(armor)  & set(items)) > 1: return False
    if len(set(rings)  & set(items)) > 2: return False
    return True


def main():
    all_items = set(wepons + rings + armor)
    Pitems = powerset(all_items)
    winnable, lossable = [], []

    for items in Pitems:
        if acceptable(items):
            player = Ent(100, 0, 0, items)
            if simulate(player): winnable.append(sum([x.cost for x in items]))
            else: lossable.append(sum([x.cost for x in items]))

    winnable.sort()
    lossable.sort()
    print(winnable[0], lossable[-1])



if __name__ == "__main__":
    main()

