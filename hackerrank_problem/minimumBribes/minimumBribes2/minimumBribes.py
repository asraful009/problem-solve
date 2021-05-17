#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
  print(q)
  insertionSort(q)
  s = 0
  # for i, v in enumerate(q):
  #   if i+1-v < 0:
  #     if i+1-v <= -3:
  #       return "Too chaotic"
  #     else:
  #       s+= -(i+1-v)
    # print(f'{i+1}:{v} => {i+1-v} {s}')
  return s


def insertionSort(arr):
  count = 0
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    tCount = 0
    while j >= 0 and key < arr[j] :
      tCount+=1
      arr[j + 1] = arr[j]
      j -= 1
    print(key, tCount)
    count+=tCount
    arr[j + 1] = key
  print (arr, count)


if __name__ == '__main__':
  t = int(input().strip())

  for t_itr in range(t):
    n = int(input().strip())

    q = list(map(int, input().rstrip().split()))

    r = minimumBribes(q)
    print(r)
