import time 

def part_1(content):
    t0 = time.time()
    
    # parsing
    times, distances = [
        [
            int(x) for x in l.split() if len(x) > 0 and x[0].isdigit()
        ] for l in content.split('\n')
    ][:-1]
    
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
    pass
    
if __name__ == "__main__":
    with open("./input_data/day_06.txt") as f:
        content = f.read()
        part_1(content)
        part_2(content)