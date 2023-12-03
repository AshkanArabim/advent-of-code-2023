import re
import time

# match anything except dots, newlines, and digits
SYMBOL_PATTERN = re.compile(r'[^\d\.\n]')

def get_full_number(coords, grid, seen_nums_grid):
    # get bounds of provided digit
    left_bound = coords[1] 
    right_bound = coords[1] + 1 
    
    # return 0 if number is already seen
    if seen_nums_grid[coords[0]][coords[1]]:
        return 0
    
    # find left bond
    while left_bound > 0 and grid[coords[0]][left_bound - 1].isdigit():
        left_bound -= 1
        seen_nums_grid[coords[0]][left_bound] = True
        
    # find right bound
    while (right_bound < len(grid[0]) and 
           grid[coords[0]][right_bound].isdigit()):
        seen_nums_grid[coords[0]][right_bound] = True
        right_bound += 1

    # return number in bounds
    return int(grid[coords[0]][left_bound : right_bound])


def part_1(content):
    t0 = time.time()
    
    # create grid
    grid = content.split('\n')[:-1]
    LINE_WIDTH = len(grid[0]) + 1 # to account for the lost \n
    
    # create grid for checked numbers
    seen_nums_grid = [[False] * len(grid[0]) for i in range(len(grid))]
    
    # find symbols and convert index to coords
    symbol_coords = [divmod(match.start(), LINE_WIDTH) for match 
                   in re.finditer(SYMBOL_PATTERN, content)]
    
    # find surrounding coords containing nums
    num_coords = []
    for symbol_coord in symbol_coords:
        for i in range(symbol_coord[0] - 1, symbol_coord[0] + 2):
            for j in range(symbol_coord[1] - 1, symbol_coord[1] + 2):
                if grid[i][j].isdigit():
                    num_coords.append((i, j))
    
    # add all part numbers, mark seen_nums_grid to avoid duplicates
    sum_part_numbers = 0
    for num_coord in num_coords:
        sum_part_numbers += get_full_number(num_coord, grid, seen_nums_grid)
        
    t1 = time.time()
        
    print("sum of part numbers:", sum_part_numbers)
    print("time taken:", "{:.5f}".format(t1 - t0))
    

def part_2(content):
    pass


if __name__ == "__main__":
    with open('./input_data/day_3.txt') as f:
        content = f.read()
        part_1(content)
        part_2(content)