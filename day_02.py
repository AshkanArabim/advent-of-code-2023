### some reminders vv

# constants: UPPERCASE
# files: snake_case
# class: PascalCase

## spacing
# ANYTHING at the root level should be double-spaced
# double quote preferred
# TWO spaces before comment

# use startswith and endswith
import re
import time

ball_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_1(content):
    t0 = time.time()
    sum_possible = 0
    
    # split into lines and groups
    # notice that I'm removing the last line
    for line_num, line in enumerate(content.split('\n')[:-1]):
        _, line = line.split(':')
        balls_in_game = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for ball_group in re.split(r',|;', line):
            count, color = ball_group.strip().split(' ')
            count = int(count)
            balls_in_game[color] = max(balls_in_game[color], count)
            
        if all(balls_in_game[color] <= ball_limits[color] 
               for color in ball_limits.keys()):
            sum_possible += line_num + 1 # starts from 0
    
    t1 = time.time()
    print("sum of possible games:", sum_possible)
    print("time taken:", t1 - t0)
    
    
def part_2():
    pass

if __name__ == "__main__":
    with open('./input_data/day_2.txt') as f:
        content = f.read()
        part_1(content)
        part_2()