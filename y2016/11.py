import itertools as it

def parse(l, element, types):
    layout = []
    for items in l:
        floor = []
        items = items.split(" ")
        for item in items:
            if item in types:
                continue
            if "compatible" in item:
                item = item[:item.rfind("-")]
                floor.append([item, "microchip"])
                continue
            if item in element:
                floor.append([item, "generator"])
                continue
        layout.append(floor)
    return layout

def hash(layout, floor_index, num):
    for item in layout:
        item.sort()
    return str(layout) + ',' + str(floor_index) + ',' + str(num)

def is_ok(item1, item2):
    if item1[1] == item2[1]: return True
    if item1[0] == item2[0]: return True
    return False

def floor_ok(floor):
    generators = set(x[0] for x in floor if x[1] == "generator")
    chips = set(x[0] for x in floor if x[1] == "microchip")
    return chips.issubset(generators) or len(generators) == 0

def layout_ok(layout):
    for item in layout:
        if not floor_ok(item): return False
    return True

def main():
    # elements = ["thulium", "plutonium", "strontium", "promethium", "ruthenium", "elerium", "dilithium"]
    elements = ["thulium", "plutonium", "strontium", "promethium", "ruthenium"]
    types = ["generator", "microchip"]

    layout = [x.strip() for x in open('input').readlines()]

    layout = parse(layout, elements, types)
    stack = [(layout, 0, 0)]
    seen = set()
    seen.add(hash(layout, 0, 0))

    def step(curr_layout, floor_index, num):
        curr_floor = curr_layout[floor_index]
        for m in [1,2]:
            for comb in it.combinations(curr_floor, m):
                if len(comb) == 1 or is_ok(*comb):
                    new_curr_floor = [x for x in curr_floor if x not in comb]
                    if floor_index > 0:
                        next_layout = [x for x in curr_layout]
                        next_layout[floor_index - 1] = [x for x in curr_layout[floor_index - 1]] + list(comb)
                        next_layout[floor_index] = new_curr_floor

                        if layout_ok(next_layout):
                            s = hash(next_layout, floor_index - 1, 0)
                            if not (s in seen):
                                stack.append((next_layout, floor_index - 1, num + 1))
                                seen.add(s)

                    if floor_index < 3:
                        next_layout = [x for x in curr_layout]
                        next_layout[floor_index + 1] = [x for x in curr_layout[floor_index + 1]] + list(comb)
                        next_layout[floor_index] = new_curr_floor
                        if layout_ok(next_layout):
                            s = hash(next_layout, floor_index + 1, 0)
                            if not (s in seen):
                                stack.append((next_layout, floor_index + 1, num + 1))
                                seen.add(s)

    while len(stack) > 0:
        curr_layout, floor, num = stack.pop(0)
        if curr_layout[0] == curr_layout[1] == curr_layout[2] == []:
            print(num, curr_layout)
        step(curr_layout, floor, num)



if __name__ == '__main__':
    main()
