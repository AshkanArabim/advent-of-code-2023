# Not using re to learn to parse efficiently
import time

def part_1(content):
    t0 = time.time()
    
    # split lines, ditch empty last line
    lines = content.split("\n")[:-1]

    sum_values = 0

    for line in lines:
        # save lucky numbers and winning numbers as strings
        lucky_nums, card_nums = line.split("|")

        # convert lucky nums to set of integers
        lucky_nums = {int(n) for n in lucky_nums.split()[2:] if len(n) > 0}

        # convert card nums to set of integers
        card_nums = {int(n) for n in card_nums.split() if len(n) > 0}

        # nums that exist in both
        common_nums = lucky_nums.intersection(card_nums)
        
        if len(common_nums) > 0:
            sum_values += 2 ** (len(common_nums) - 1)
            
    t1 = time.time()
    print("sum_values:", sum_values)
    print("time taken:", t1-t0)
    


def part_2(content):
    pass


if __name__ == "__main__":
    with open("./input_data/day_4.txt") as f:
        content = f.read()
        part_1(content)
        part_2(content)
