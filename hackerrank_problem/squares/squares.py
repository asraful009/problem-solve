#!/bin/python3

import math
import os
import random
import re
import sys

def squares(a, b):
  x = math.ceil(math.sqrt(a))
  y = math.floor(math.sqrt(b))+1
  # print(f'[{a}, {b}] -> [{x}, {y}] = { y-x }')
  return y-x

if __name__ == '__main__':
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')
  fptr = open("m.txt", 'w')
  q = int(input().strip())
  for q_itr in range(q):
    first_multiple_input = input().rstrip().split()
    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])
    result = squares(a, b)
    fptr.write(str(result) + '\n')
  fptr.close()
