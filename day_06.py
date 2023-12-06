import time 
import numpy as np

def part_1(content):
    t0 = time.time()
    
    # parsing
    times, distances = [
        [
            int(x) for x in l.split() if len(x) > 0 and x[0].isdigit()
        ] for l in content.split('\n') if len(l) > 0
    ]
    
    # iterate over values to find all margins of error
    margins_of_error = 1 # because we are multiplying
    for i in range(len(times)):
        # iterate over all possible button-holding times
        num_wins = 0
        for hold_time in range(times[i] + 1):
            if hold_time * (times[i] - hold_time) > distances[i]:
                num_wins += 1
        margins_of_error *= num_wins
        
    t1 = time.time()
    print("margins of error:", margins_of_error)
    print("time taken:", "{:.5f}".format(t1 - t0))


def part_2(content):
    t0 = time.time()
    
    # parsing
    t, d = [
        int("".join([
            x for x in l.split() if len(x) > 0 and x[0].isdigit()
        ])) for l in content.split('\n') if len(l) > 0
    ]
    
    # get times to have a distance equal to target (used algebra)
    # top = t + np.sqrt(t ** 2 - 4 * 1 * (-d)) / 2
    # bottom = t - np.sqrt(t ** 2 - 4 * 1 * (-d)) / 2
    
    top = (-t - np.sqrt(t ** 2 - 4 * (-1) * (-d))) / (-2)
    bottom = (-t + np.sqrt(t ** 2 - 4 * (-1) * (-d))) / (-2)
    
    # if bounds have no remainders, add / subtract 1 to that we're winning
    # if not, make them ints (round up or down depending on bound)
    top = top - 1 if top % 1 == 0 else np.floor(top)
    bottom = bottom + 1 if bottom % 1 == 0 else np.ceil(bottom)
    
    ways_to_win = top - bottom + 1 # all the ways we can win
    
    t1 = time.time()
    print("ways to win:", ways_to_win)
    print("time taken:", "{:.5f}".format(t1 - t0))
    
    
if __name__ == "__main__":
    with open("input_data/day_06.txt") as f:
        content = f.read()
        part_1(content)
        part_2(content)