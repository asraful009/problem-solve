#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def cap(x) :
  return x.capitalize()

def solve(s):
  arr = []
  for x in s.split(" "):
    # print(f"{x} -> {cap(x)}")
    arr.append(cap(x))
  r = " ".join(arr)
  # print(r)
  return r


if __name__ == '__main__':
  os.environ['OUTPUT_PATH'] = "o.txt"
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = solve(s)

  fptr.write(result + '\n')

  fptr.close()
