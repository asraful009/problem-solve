#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    # print("{} {} {}".format(i, j, k))
    m = 0
    for v in range(i, j+1):
        num = v
        a = 0
        while(num > 0):
            remainder = num % 10
            a = (a * 10) + remainder
            num = num//10
        # print("{} {} {} {}".format(v, a, abs(v - a), abs(v - a) % k))
        if abs(v - a) % k == 0:
            m += 1
    # print(m)
    return m

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
