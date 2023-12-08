import time


# returns list of tuples: (hand, bid)
def parse(content):
    return [
        tuple(x for x in line.split()) for line in content.split('\n')[:-1]
    ]


def part_1(content):
    content = parse(content)
    
    # split into lists of hand types
    hand_types = [[] for i in range(7)]
    for hand, bid in content:
        letter_counts = {}
        power_idx = None
        
        for l in hand:
            if l not in letter_counts:
                letter_counts[l] = 0
            letter_counts[l] += 1
            
        if len(letter_counts) == 1:
            power_idx = 0 # five of a kind
        elif len(letter_counts) == 2:
            if 1 in letter_counts.values():
                power_idx = 1 # four of a kind
            else:
                power_idx = 2 # full house
        elif len(letter_counts) == 3:
            if 3 in letter_counts.values():
                power_idx = 3 # three of a kind
            else:
                power_idx = 4 # two pair
        elif len(letter_counts) == 4:
            power_idx = 5
        else:
            power_idx = 6
            
        hand_types[power_idx].append((hand, int(bid)))
        
    # sort each hand type in order of card strength
    # e.g. AAAAA is first in five-of-a-type group
    CARD_PRIORITY = {
        letter : strength + 1 for strength, letter in enumerate([
            'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'
        ])
    }
    
    for i in range(len(hand_types)):
        hand_types[i].sort(key=lambda pair: [CARD_PRIORITY[l] for l in pair[0]])
    
    # multiply every bid by the index down that it's sorted
    
    sum = 0
    i = len(content)
    for group in hand_types:
        for hand, bid in group:
            # best hand should get highest multiplication
            sum += i * bid
            i -= 1
    
    return sum
    

def part_2(content):
    content = parse(content)
    
    # split into lists of hand types
    hand_types = [[] for i in range(7)]
    for hand, bid in content:
        letter_counts = {}
        power_idx = None
        
        # remove any Js.         
        for l in hand.replace('J', ''):
            if l not in letter_counts:
                letter_counts[l] = 0
            letter_counts[l] += 1
        
        if len(letter_counts) in [0, 1]:
            power_idx = 0 # five of a kind
        elif len(letter_counts) == 2:
            if 1 in letter_counts.values():
                power_idx = 1 # four of a kind
            else:
                power_idx = 2 # full house
        elif len(letter_counts) == 3: 
            # if there are two 1s in values. 
            # adjusted to accomodate for removed 'J'
            if list(letter_counts.values()).count(1) >= 2: 
                power_idx = 3 # three of a kind
            else:
                power_idx = 4 # two pair
        elif len(letter_counts) == 4:
            power_idx = 5
        else:
            power_idx = 6
            
        hand_types[power_idx].append((hand, int(bid)))    
    
    # sort each hand type in order of card strength
    # but now 'J' is the most worthless
    CARD_PRIORITY = {
        letter : strength + 1 for strength, letter in enumerate([
            'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'
        ])
    }
    
    for i in range(len(hand_types)):
        hand_types[i].sort(key=lambda pair: [CARD_PRIORITY[l] for l in pair[0]])
    
    # multiply every bid by the index down that it's sorted
    
    sum = 0
    i = len(content)
    for group in hand_types:
        for hand, bid in group:
            # best hand should get highest multiplication
            sum += i * bid
            i -= 1
    
    return sum


if __name__ == "__main__":
    with open("./input_data/day_07.txt") as f:
        content = f.read()
        for part in [part_1, part_2]:
            t0 = time.time()
            res = part(content)
            t1 = time.time()
            print("result:", res)
            print("time taken:", "{:.5f}".format(t1 - t0))