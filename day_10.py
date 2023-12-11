import time


IDX_TO_DIR = ["top", "right", "bottom", "left"]


DIR_TO_CHARS = {
    "top": {'F', '|', '7'},
    "right": {'J', '-', '7'},
    "bottom": {'J', '|', 'L'},
    "left": {'F', '-', 'L'}
}


CHAR_TO_DIRS = {
    'S': {"top", "right", "bottom", "left"},
    'F': {"bottom", "right"},
    '|': {"top", "bottom"},
    '7': {"bottom", "left"},
    '-': {"right", "left"},
    'J': {"top", "left"},
    'L': {"top", "right"}
}


def find_s(content):
    for i in range(len(content)):
        for j in range(len(content[0])):
            if content[i][j] == 'S':
                return (i, j)
            

def parse(content):
    content = content.split('\n')[:-1]
    return (content, find_s(content))


def part_1(content):
    content, s_coord = parse(content)
    lim_i = len(content)
    lim_j = len(content[0])
    
    # find
    curr_coord = s_coord
    seen = set()
    while(True):
        seen.add(curr_coord)
        curr_ltr = content[curr_coord[0]][curr_coord[1]]
        next_coords = []
        for i, adj_coord in enumerate([
            (curr_coord[0] - 1, curr_coord[1]), # up
            (curr_coord[0], curr_coord[1] + 1), # right
            (curr_coord[0] + 1, curr_coord[1]), # bottom
            (curr_coord[0], curr_coord[1] - 1)  # left
        ]):
            # remove out-of-bound coords
            if (any(x < 0 for x in adj_coord) or
                adj_coord[0] >= lim_i or 
                adj_coord[1] >= lim_j
            ):
                continue
            
            adj_ltr = content[adj_coord[0]][adj_coord[1]]
            dir = IDX_TO_DIR[i]
            
            # check if this direction is possible for this letter
            if dir not in CHAR_TO_DIRS[curr_ltr]:
                continue
            
            # check if adj_ltr connects in this direction
            if adj_ltr not in DIR_TO_CHARS[dir]:
                continue
            
            # remove seen coords
            if adj_coord in seen:
                continue
            
            next_coords.append(adj_coord)
                
        if len(next_coords) == 0:
            break # no more new paths left
        # go to the first coord that isn't seen and is valid
        curr_coord = next_coords[0]
        
    return len(seen) // 2


def part_2(content):
    pass


if __name__ == "__main__":
    with open("./input_data/day_10.txt") as f:
        content = f.read()
        for part in [part_1, part_2]:
            t0 = time.time()
            res = part(content)
            t1 = time.time()
            print("result:", res)
            print("time taken:", "{:.5f}".format(t1 - t0))
