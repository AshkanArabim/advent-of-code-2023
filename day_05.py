import time


def part_1(content):
    t0 = time.time()
    
    
    # load seeds and maps
    seeds, *maps = [x for x in content.split("\n\n")]

    # convert seeds to ints; ditch first element "seeds:"
    seeds = [int(x) for x in seeds.split()[1:]]

    # convert map string entries to (start, end, shift)
    for i in range(len(maps)):
        # 2d list of integers
        maps[i] = [
            [int(x) for x in l.split()] for l in maps[i].split("\n")[1:] if len(l) > 0
        ]
        
        pass # DEBUG
    # confirmed marker ^
        # convert to tuples (start, end, shift)
        maps[i] = [(l[1], l[1] + l[2], l[0] - l[1]) for l in maps[i]]

    # find min final position
    min_position = float('inf')
    for seed in seeds:
        for m in maps:
            for l in m: # see if seed falls in the range of a map entry
                if seed >= l[0] and seed < l[1]:
                    seed += l[2] # shift the seed
                    # break inner loop with first match found
                    break
        min_position = min(seed, min_position)
        
    t1 = time.time()
    print("min position:", min_position)
    print("time taken:", "{:.5f}".format(t1 - t0))


def part_2(content):
    pass


if __name__ == "__main__":
    with open("./input_data/day_5.txt") as f:
        content = f.read()
        part_1(content)
        part_2(content)
