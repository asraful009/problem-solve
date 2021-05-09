#!/bin/python3

import math
import os
import random
import re
import sys



def jumpingOnClouds(c, k):
  # print(f'{c} => {k}')
  n = len(c)
  i, s = k%n, 100
  s -= (c[i] * 2 + 1)
  while i != 0:
    i=( i + k ) % n
    s -= ( c[i] * 2 + 1 )
  # print(s)
  return s

if __name__ == '__main__':
  # fptr = open(".my.txt", 'w')
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  nk = input().split()
  n = int(nk[0])
  k = int(nk[1])
  c = list(map(int, input().rstrip().split()))
  result = jumpingOnClouds(c, k)
  fptr.write(str(result) + '\n')
  fptr.close()
