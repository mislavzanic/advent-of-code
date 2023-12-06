from collections import defaultdict

def main(day):
    seeds = []
    maps = defaultdict(list)
    curr_map = None
    map_types = []
    for line in day.lines():
        if line.startswith("seeds:"):
            seeds = [x for x in map(int, line.split(": ")[1].split(" "))]
            continue
        if line == "": continue
        if "map" in line:
            curr_map = line.split(" ")[0]
            map_types.append(curr_map)
            continue

        maps[curr_map].append([x for x in map(int, line.split(" "))])


    curr_iter = [x for x in seeds]
    for pair in map_types:
        next_iter = []
        for seed in curr_iter:
            ok = False
            for rg in maps[pair]:
                if rg[1] <= seed <= rg[1] + rg[2]:
                    next_iter.append(rg[0] + (seed - rg[1]))
                    ok = True
                    break
            if not ok:
                next_iter.append(seed)
        curr_iter = [x for x in next_iter]


    for pair in map_types:
        for i, p1 in enumerate(maps[pair]):
            for j, p2 in enumerate(maps[pair]):
                if i != j and p1 == p2: assert False

    print(min(curr_iter))

    curr_iter = {seeds[i] : seeds[i+1] for i in range(0,len(seeds), 2)}
    for pair in map_types:
        next_iter = {}
        while len(curr_iter) > 0:
            seed, rg_seed = curr_iter.popitem()
            ok = False
            for rg in maps[pair]:
                if rg[1] <= seed and seed + rg_seed <= rg[1] + rg[2]:
                    next_iter[rg[0] + seed - rg[1]] = rg_seed
                    ok = True
                    break

                if rg[1] <= seed < rg[1] + rg[2] and rg[1] + rg[2] < seed + rg_seed:
                    next_iter[rg[0] + seed - rg[1]] = rg[1] + rg[2] - seed
                    curr_iter[rg[1] + rg[2]] = seed + rg_seed - rg[1] - rg[2]
                    ok = True
                    break

                if seed < rg[1] and rg[1] < seed + rg_seed <= rg[1] + rg[2]:
                    next_iter[rg[0]] = seed + rg_seed - rg[1]
                    curr_iter[seed] = rg[1] - seed
                    ok = True
                    break

                if seed < rg[1] and rg[1] + rg[2] < seed + rg_seed:
                    next_iter[rg[0]] = rg[2]
                    curr_iter[seed] = rg[1] - seed
                    curr_iter[rg[1] + rg[2]] = seed + rg_seed - rg[1] - rg[2]
                    ok = True
                    break

            if not ok:
                next_iter.update({seed: rg_seed})
        curr_iter = {k:v for k,v in next_iter.items()}
    print(min(curr_iter.keys()))
            
            

