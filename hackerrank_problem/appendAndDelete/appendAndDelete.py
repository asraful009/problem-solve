#!/bin/python3

import math
import os
import random
import re
import sys


def appendAndDeleteMine(s, t, k):
  # print(s, t, k)
  N = 'No'
  Y = 'Yes'
  r = N
  isSHasStr = True
  tIndex = 0
  lT = len(t) + len(s)
  if lT <= k:
    r = Y
  elif s == t:
    r = Y
  else:
    i=0
    while i<len(t):
      if i<len(s) and s[i] == t[i]:
        i+=1
      else:
        break
    print(f'{k} {len(t)-i} {len(s) -i -k }')
    
    if k>=len(t)-i and len(s) -i <k:
      r = Y
  print(r)
  return r


def appendAndDelete(s, t, k):
  i=0
  while i<min(len(s), len(t)):
    if s[i] == t[i]:
      i+=1
    else:
      break
  if len(s) + len(t) - 2*i > k:
    return "No"
  elif (len(s) + len(t) - 2*i)%2 == k%2:
    return "Yes"
  elif len(s) + len(t) -k <0 :
    return "Yes"
  else:
    return "No"


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  # fptr = open(".m.txt", 'w')

  s = input()

  t = input()

  k = int(input().strip())

  result = appendAndDelete(s, t, k)
  # print(result)
  fptr.write(result + '\n')

  fptr.close()
