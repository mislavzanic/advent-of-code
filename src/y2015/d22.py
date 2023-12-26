from aoc_util.advent import Input

def apply_stats(ent):
    effects = {
        'recharge': ('mana', 101),
        'poison': ('hp', -3),
    }

    for k,v in effects.items():
        if k in ent and ent[k] > 0:
            stat, val = v
            ent[k] -= 1
            ent[stat] += val

    if 'shield' in ent:
        ent['shield'] = max(0, ent['shield'] - 1)

    return ent

def parse(day: Input):
    start_me, start_enemy = {
        'hp': 50,
        'mana': 500,
        'cost': 0,
        'shield': 0,
        'recharge': 0,
        'armor': 0
    }, {
        'poison': 0,
    }

    for line in day.lines():
        key, value = line.split(': ')
        if key == 'Hit Points': start_enemy['hp'] = int(value)
        else: start_enemy['dmg'] = int(value)

    attacks = [
        {'cost': 53,  'mana': -53,  'dmg': 4, 'heal': 0, 'shield': 0, 'recharge': 0, 'poison': 0},
        {'cost': 73,  'mana': -73,  'dmg': 2, 'heal': 2, 'shield': 0, 'recharge': 0, 'poison': 0},
        {'cost': 113, 'mana': -113, 'dmg': 0, 'heal': 0, 'shield': 6, 'recharge': 0, 'poison': 0},
        {'cost': 229, 'mana': -229, 'dmg': 0, 'heal': 0, 'shield': 0, 'recharge': 5, 'poison': 0},
        {'cost': 173, 'mana': -173, 'dmg': 0, 'heal': 0, 'shield': 0, 'recharge': 0, 'poison': 6},
    ]

    return start_me, start_enemy, attacks

def bfs(start_me, start_enemy, attacks, difficulty='easy'):
    Q = [(start_me, start_enemy, 0)]
    m = 10**9
    while Q:
        me, enemy, turn = Q.pop(0)
        if m <= me['cost']: continue
        if turn % 2 == 0: me['hp'] -= 1 * int(difficulty == 'hard')
        if me['hp'] <= 0: continue

        me = apply_stats(me)
        enemy = apply_stats(enemy)

        if enemy['hp'] <= 0:
            if m > me['cost']:
                m = me['cost']
            continue

        if turn % 2 == 1:
            me['hp'] -= max(enemy['dmg'] - 7 * int(me['shield'] > 0), 1)
            Q.append((me, enemy, turn + 1))
            continue

        for attack in attacks:
            if me['mana'] < attack['cost']:
                continue

            if any(attack[k] > 0 and k in me and me[k] > 0 for k in ['shield', 'recharge', 'poison']):
                continue
            if any(attack[k] > 0 and k in enemy and enemy[k] > 0 for k in ['shield', 'recharge', 'poison']):
                continue

            new_me = {k:v for k,v in me.items()}
            new_enemy = {k:v for k,v in enemy.items()}

            for k,v in attack.items():

                if k == 'dmg':
                    new_enemy['hp'] -= v
                    continue

                if k == 'heal':
                    new_me['hp'] += v
                    continue

                if k in me:
                    new_me[k] += v
                else:
                    new_enemy[k] += v

            Q.append((new_me, new_enemy, turn + 1))
    return m

def p2(day: Input):
    start_me, start_enemy, attacks = parse(day)
    return bfs(start_me, start_enemy, attacks, 'hard')

def p1(day: Input):
    start_me, start_enemy, attacks = parse(day)
    return bfs(start_me, start_enemy, attacks)


