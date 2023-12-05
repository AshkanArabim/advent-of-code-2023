# Not using re to learn to parse efficiently
import time


def part_1(content):
    t0 = time.time()
    sum_values = 0

    # split lines, ditch empty last line
    for line in content.split("\n")[:-1]:
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
    print("time taken:", "{:.5f}".format(t1 - t0))


def part_2(content):
    t0 = time.time()
    sum_cards = 0

    # parse content to dictionary
    cards = {}
    lines = content.split("\n")[:-1]
    max_key = len(lines)
    for i, line in enumerate(lines):
        # save lucky numbers and winning numbers as strings
        lucky_nums, card_nums = line.split("|")

        # convert lucky nums to set of integers
        lucky_nums = {int(n) for n in lucky_nums.split()[2:] if len(n) > 0}

        # convert card nums to set of integers
        card_nums = {int(n) for n in card_nums.split() if len(n) > 0}

        # {card_idx: (count, num_matches)}
        cards[i + 1] = [1, len(lucky_nums.intersection(card_nums))]

    # count copies and add to sum
    for i in range(1, max_key + 1):
        sum_cards += cards[i][0]

        # add num of cards to next n cards
        for j in range(i + 1, i + cards[i][1] + 1):
            if j > max_key:
                break
            cards[j][0] += cards[i][0]

    t1 = time.time()
    print("sum of cards:", sum_cards)
    print("time taken:", "{:.5f}".format(t1 - t0))


if __name__ == "__main__":
    with open("./input_data/day_4.txt") as f:
        content = f.read()
        part_1(content)
        part_2(content)
