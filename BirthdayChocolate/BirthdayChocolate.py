#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    totalCount = 0
    l = len(s)
    # print("{} {} {}".format(s, d, m))
    for i in range(l):
        sv = 0
        for j in range(i, i+m):
            if(l == j):
                break
            # print("sv[{}, {}] : {} > {} >> {}".format(i, j, sv, s[j], abs(j-i+1)))
            sv += s[j]
            if sv == d and abs(j-i+1) == m:
                totalCount += 1
                # print("find => sv[{}, {}] : {} -> {}".format(i, j, sv, totalCount))
                break
    # print("count :{}".format(totalCount))
    return totalCount

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
