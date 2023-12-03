# running time: 0.00429081916809082

import re
import time

t0 = time.time()
running_sum = 0
with open('./input.txt', 'r') as f:
  content = f.read()
  
  # get indices of newlines
  # adding a -1 to assume there is a newline before the first line
  newlines = [-1] + [match.start() for match in re.finditer('\n', content)]
  
  # get line bounds
  # (idx of first letter in line, idx of \n at the end of line)
  bounds = [(newlines[i], newlines[i+1]) for i in range(len(newlines) - 1)]
  
  # for loop to check between newlines (end inclusive)
  for bound in bounds:
    num = 0
    # ltr iterate --> add first digit 
    for i in range(bound[0], bound[1]):
      # if digit
      ascii_char = ord(content[i])
      if 48 <= ascii_char <= 57:
        num += (ascii_char - 48) * 10
        break
    # rtl iterate --> add second digit 
    for i in range(bound[1], bound[0], -1):
      # if digit
      ascii_char = ord(content[i])
      if 48 <= ascii_char <= 57:
        num += ascii_char - 48
        break
    # running_sun += num
    running_sum += num

t1 = time.time()
  
print("part 1 answer:", running_sum)
print("time taken:", t1 - t0)