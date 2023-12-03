import re
import time
from functools import reduce

BALL_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def part_1(content):
    t0 = time.time()
    sum_possible = 0
    
    # split into lines and groups
    # notice that I'm removing the last line due it it being empty
    for line_num, line in enumerate(content.split('\n')[:-1]):
        _, line = line.split(':')
        balls_in_game = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for ball_group in re.split(r',|;', line):
            count, color = ball_group.strip().split(' ')
            balls_in_game[color] = max(balls_in_game[color], int(count))
            
        if all(balls_in_game[color] <= BALL_LIMITS[color] 
               for color in BALL_LIMITS.keys()):
            sum_possible += line_num + 1 # starts from 0
    
    t1 = time.time()
    print("sum of possible games:", sum_possible)
    print("time taken:", "{:.5f}".format(t1 - t0))
    
    
def part_2(content):
    t0 = time.time()
    sum_powers = 0
    
    for line in content.split('\n')[:-1]:
        _, line = line.split(':')
        min_balls_in_game = {
            "red": 0, 
            "green": 0,
            "blue": 0
        }
        for ball_group in re.split(r',|;', line):
            count, color = ball_group.strip().split(' ')
            min_balls_in_game[color] = max(min_balls_in_game[color], int(count))
            
        sum_powers += reduce((lambda x, y: x * y), min_balls_in_game.values())
    
    t1 = time.time()
    print("sum of powers:", sum_powers)
    print("time taken:", "{:.5f}".format(t1 - t0))
    

if __name__ == "__main__":
    with open('./input_data/day_2.txt') as f:
        content = f.read()
        part_1(content)
        part_2(content)
