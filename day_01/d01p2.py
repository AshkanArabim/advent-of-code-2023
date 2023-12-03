# running time: 0.00548

import re
import time

t0 = time.time()
running_sum = 0
with open('./input.txt', 'r') as f:
  content = f.read()
  
  # find all spelled-out numbers
  spell_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
  }
  spelled_num_pattern = re.compile(r"(?=(" + r"|".join(spell_to_num.keys()) + r"))")  
  spelled_matches = {match.start(): match.group(1) for match in re.finditer(
    spelled_num_pattern, content
  )}
  
  # get indices of newlines
  # adding a -1 to assume there is a newline before the first line
  newlines = [-1] + [match.start() for match in re.finditer('\n', content)]
  
  # get line bounds
  # (newline before line, newline at end of line)
  bounds = [(newlines[i], newlines[i+1]) for i in range(len(newlines) - 1)]
  
  # for loop to check between newlines (end inclusive)
  for bound in bounds:
    num = 0
    # ltr iterate --> add first digit 
    for i in range(bound[0] + 1, bound[1]):
      # if spelled digit
      if i in spelled_matches:
        num += spell_to_num[spelled_matches[i]] * 10
        break
      
      # if digit
      ascii_char = ord(content[i])
      if 48 <= ascii_char <= 57:
        num += (ascii_char - 48) * 10
        break
      
    # rtl iterate --> add second digit
    for i in range(bound[1] - 1, bound[0], -1):
      # if spelled digit
      if i in spelled_matches:
        num += spell_to_num[spelled_matches[i]]
        break
      
      # if digit
      ascii_char = ord(content[i])
      if 48 <= ascii_char <= 57:
        num += ascii_char - 48
        break
    # running_sun += num
    running_sum += num

t1 = time.time()
  
print("part 2 answer:", running_sum)
print("time taken:", "{:.5f}".format(t1 - t0))