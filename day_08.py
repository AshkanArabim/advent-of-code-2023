import time
import numpy as np

def parse(content):
    steps, nexts = content.split('\n\n')
    
    d = {}
    for line in nexts.split('\n')[:-1]:
        key, val = line.split(' = ')
        d[key] = tuple(val[1:-1].split(', '))
    
    return steps, d
    

def part_1(content):
    steps, d = parse(content) # parse content
    
    loc = "AAA"
    step_idx = 0
    step_count = 0
    while loc != "ZZZ":
        # go to next step
        dir_idx = 0 if steps[step_idx] == 'L' else 1
        loc = d[loc][dir_idx]
        
        step_idx = (step_idx + 1) % len(steps) # steps roll over
        step_count += 1
    
    return step_count


def part_2(content):
    steps, d = parse(content)
    
    loc = [node for node in d.keys() if node[-1] == 'A']
    
    loc_step_count = [0] * len(loc)
    for i, l in enumerate(loc):
        
        step_idx = 0
        step_count = 0
        while l[-1] != 'Z':
            dir_idx = 0 if steps[step_idx] == 'L' else 1
            l = d[l][dir_idx]
        
            step_idx = (step_idx + 1) % len(steps)
            step_count += 1
            
        loc_step_count[i] = step_count
        
    return np.lcm.reduce(loc_step_count)


if __name__ == "__main__":
    with open("./input_data/day_08.txt") as f:
        content = f.read()
        for part in [part_1, part_2]:
            t0 = time.time()
            res = part(content)
            t1 = time.time()
            print("result:", res)
            print("time taken:", "{:.5f}".format(t1 - t0))
