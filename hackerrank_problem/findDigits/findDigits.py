#!/bin/python3

import math
import os
import random
import re
import sys


def findDigits(n):
  dig = f'{n}'
  count = 0
  for i in dig:
    m = int(i)
    if m != 0 and n % m == 0:
      count+=1
  # print(count)
  return count

if __name__ == '__main__':
  # fptr = open("./my.txt", 'w')
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  t = int(input().strip())
  for t_itr in range(t):
    n = int(input().strip())
    result = findDigits(n)
    fptr.write(str(result) + '\n')
  fptr.close()
