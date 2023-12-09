import time


def parse(content):
    return [[int(x) for x in line.split()] for line in content.split('\n')[:-1]]


def part_1(content):
    # parse into list of lists of ints
    content = parse(content)
    
    # for each line
    sum_next_histories = 0
    for line in content:
        derivatives = [line]
        while len(set(derivatives[-1])) != 1 or derivatives[-1][0] != 0:
            derivatives.append(
                [y - x for x, y in zip(
                    derivatives[-1][:-1], derivatives[-1][1:]
                )]
            )
        
        # add zero to 0 sequence
        derivatives[-1].append(0) 
        # get next iterm in main sequence
        for diff_idx, orig_idx in reversed(list(zip(
            range(1, len(derivatives)), range(len(derivatives) - 1)
        ))): 
            # add next element to original list by adding element from diff list
            derivatives[orig_idx].append(
                derivatives[orig_idx][-1] + derivatives[diff_idx][-1]
            )
        
        # add last element of original sequence to sum
        sum_next_histories += derivatives[0][-1]

    return sum_next_histories

def part_2(content):
    # parse into list of lists of ints
    content = parse(content)
    
    # for each line
    sum_previous_histories = 0
    for line in content:
        derivatives = [line]
        while len(set(derivatives[-1])) != 1 or derivatives[-1][0] != 0:
            derivatives.append(
                [y - x for x, y in zip(
                    derivatives[-1][:-1], derivatives[-1][1:]
                )]
            )
        
        # add zero to 0 sequence
        # we don't care where a new zero is added
        derivatives[-1].append(0) 
        
        # get previous iterm in main sequence
        for diff_idx, orig_idx in reversed(list(zip(
            range(1, len(derivatives)), range(len(derivatives) - 1)
        ))): 
            # weird hack to avoid inserting with O(n)
            # for each list, put first element at the end!
            derivatives[orig_idx].append(
                derivatives[orig_idx][0] - derivatives[diff_idx][-1]
            )
        
        # add last element of original sequence to sum
        sum_previous_histories += derivatives[0][-1]

    return sum_previous_histories


if __name__ == "__main__":
    with open("./input_data/day_09.txt") as f:
        content = f.read()
        for part in [part_1, part_2]:
            t0 = time.time()
            res = part(content)
            t1 = time.time()
            print("result:", res)
            print("time taken:", "{:.5f}".format(t1 - t0))
