import re
import time

# match anything except dots, newlines, and digits
SYMBOL_PATTERN = re.compile(r'[^\d\.\n]')

def get_full_number(coords, grid, seen_nums_grid, return_seen_coords=False):
    seen_coords = []
    
    # get bounds of provided digit
    left_bound = coords[1] 
    right_bound = coords[1] + 1 
    
    # return 0 if number is already seen
    if seen_nums_grid[coords[0]][coords[1]]:
        if return_seen_coords:
            return 0, seen_coords
        return 0
    
    # find left bond
    while left_bound > 0 and grid[coords[0]][left_bound - 1].isdigit():
        left_bound -= 1
        seen_nums_grid[coords[0]][left_bound] = True
        if return_seen_coords:
            seen_coords.append((coords[0], left_bound))
        
    # find right bound
    while (right_bound < len(grid[0]) and 
           grid[coords[0]][right_bound].isdigit()):
        seen_nums_grid[coords[0]][right_bound] = True
        if return_seen_coords:
            seen_coords.append((coords[0], right_bound))
        right_bound += 1

    # return number in bounds
    if return_seen_coords:
        return int(grid[coords[0]][left_bound : right_bound]), seen_coords
    
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
    t0 = time.time()
    
    # create grid
    grid = content.split('\n')[:-1]
    LINE_WIDTH = len(grid[0]) + 1 # to account for the lost \n
    
    # create grid for checked numbers
    seen_nums_grid = [[False] * len(grid[0]) for i in range(len(grid))]
    
    # find stars
    star_coords = [divmod(match.start(), LINE_WIDTH) for match 
                     in re.finditer("\*", content)]
    
    # DONE: a way to quickly reset the seen grid around the cell??
    # TODO: but I only want to reset when all surrounding content is done
    
    sum_gear_ratios = 0
    for star_coord in star_coords:
        nums = [] # will store nums adjacent to star
        seen_coords = []
        for i in range(star_coord[0] - 1, star_coord[0] + 2):
            for j in range(star_coord[1] - 1, star_coord[1] + 2):
                if grid[i][j].isdigit():
                    num, cell_seen_coords = get_full_number(
                        (i, j), grid, seen_nums_grid, True
                    )
                    if num != 0: 
                        nums.append(num)
                    seen_coords += cell_seen_coords
        # set seen coords back to false for next round
        for seen_coord in seen_coords:
            seen_nums_grid[seen_coord[0]][seen_coord[1]] = False
        if len(nums) == 2:
            # if it's a gear, add gear ratio to sum
            sum_gear_ratios += nums[0] * nums[1]
    
    t1 = time.time()
    print("sum of gear ratios:", sum_gear_ratios)
    print("time taken:", "{:.5f}".format(t1 - t0))

if __name__ == "__main__":
    with open('./input_data/day_3.txt') as f:
        content = f.read()
        part_1(content)
        part_2(content)