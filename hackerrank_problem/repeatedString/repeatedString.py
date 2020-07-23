#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    i=0
    j=0
    l = len(s)
    o = ""
    count = 0
    i=0
    while i<l:
        if s[i] == 'a' : 
            count += 1
        # print(s[i], count)
        i += 1
    # print(count)
    # print("{} // {}".format(n, l))
    tc = (n//l) * count
    m = n % l
    i=0
    while i<m:
        if s[i] == 'a':
            tc += 1
        i += 1
    # print("{}".format(count, tc))

    return tc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
