import time
import numpy as np


def parse(content):
    # convert to grid
    return [row for row in content.split("\n")[:-1]]


def sum_distances(content, expansion_rate):    
    content = parse(content)

    # find empty rows
    e_rows = set(
        i
        for i in range(len(content))
        if len(set(content[i])) == 1 and content[i][0] == "."
    )

    # find empty cols
    e_cols = set(
        j
        for j in range(len(content[0]))
        if len(set(content[x][j] for x in range(len(content)))) == 1
        and content[0][j] == "."
    )

    # find all star coords
    star_coords = []
    for i in range(len(content)):
        for j in range(len(content[0])):
            if content[i][j] == "#":
                star_coords.append((i, j))

    # get distances
    sum_distances = 0
    for i, first in enumerate(star_coords[:-1]):
        for second in star_coords[i + 1 :]:
            # count empty rows between stars
            num_e_rows_btwn = sum(
                1
                for _ in range(min(first[0], second[0]) + 1, max(first[0], second[0]))
                if _ in e_rows
            )

            # count empty cols between stars
            num_e_cols_btwn = sum(
                1
                for _ in range(min(first[1], second[1]) + 1, max(first[1], second[1]))
                if _ in e_cols
            )

            # get distance (horiz + vert + expanded_horiz + expanded_vert)
            sum_distances += (
                # no that here vv, we already have one or / col. itself!
                (num_e_cols_btwn + num_e_rows_btwn) * (expansion_rate - 1)
                + np.abs(first[0] - second[0]) # vert
                + np.abs(first[1] - second[1]) # horiz
            )

    return sum_distances


def part_1(content):
    return sum_distances(content, 2)


def part_2(content):
    return sum_distances(content, 1000000)

if __name__ == "__main__":
    with open("./input_data/day_11.txt") as f:
        content = f.read()
        for part in [part_1, part_2]:
            t0 = time.time()
            res = part(content)
            t1 = time.time()
            print("result:", res)
            print("time taken:", "{:.5f}".format(t1 - t0))
