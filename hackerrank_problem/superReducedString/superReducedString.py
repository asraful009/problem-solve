#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
  print(s)
  l = len(s)
  i=l-1
  t = ""
  while i>=0:
    # print(f"{i}/{l} : {s[i]} {s[i-1]} {s}")
    if s[i] == s[i-1] :
      # print(f"'{s[0:i-1 if i-1>-1 else 0]}' + '{s[i+1:] if i+1<l else ''}'")
      s = (s[0:i-1 if i-1>-1 else 0]) + (s[i+1:] if i+1<l else '')
      l = len(s)
      i =l
      # break
    i-=1
  # print(s)
  l = len(s)
  if l == 0:
    return "Empty String"
  return s

  # if True :
  #   return 'Empty String'
if __name__ == '__main__':
  fptr = open("./my.txt", 'w')
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = superReducedString(s)
  # print(result)
  fptr.write(result + '\n')

  fptr.close()
