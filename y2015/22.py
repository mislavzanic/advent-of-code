#!/usr/bin/env python3

class Ent:
    def __init__(self, hp, dmg, mana, spells):
        self.hp = hp
        self.dmg = dmg
        self.mana = mana
        self.spells = spells
        self.effects = dict()

    def get_most_dmg(self, other):
        if self.spells is None: return None
        if other.effects["Poison"] == 0: return self.spells["Poison"]
        return self.spells["MagicMissile"]

    def armor(self):
        if self.spells is None: return 0
        return 0 if "Shield" not in self.effects else self.effects["Shield"]

    def apply_effects(self):
        for k,v in self.effects.items():
            if v != 0:
                if k == "Poison":
                    self.hp -= 3
                elif k == "Recharge":
                    self.mana += 101
                self.effects[k] -= 1

    def missin_mana(self):
        ...

    def turn(self, other):
        self.apply_effects()
        other.apply_effects()

        if self.hp <= 0:
            return False
        if other.hp <= 0:
            return True

        if self.spells is None:
            a = 1 if self.dmg - other.armor() <= 1 else self.dmg - other.armor()
            other.hp -= a
            return

        if self.missin_mana():
            if not any(self.effects.values()):
                return False
            self.effects["Recharge"] += 5
            self.mana -= 229
            return

        if self.can_kill(other):
            ...
            return

        if self.will_die(other):
            ...
            return

        a = self.get_most_dmg(other)
        if other.hp - a <= 0:
            other.hp -= a
            return

        if other.dmg - self.hp <= 0:
            self.protect()





def main():
    boss = Ent(58, 9, -1, None)
    mgc = Ent(50, 0, 500, [])

    ...

if __name__ == '__main__':
    main()
