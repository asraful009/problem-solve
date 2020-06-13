#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    l = len(s)
    for i in range(l):
        sv = 0
        for j in range(m):
            print("{} {} {} {}".format(sv, i, j, s[i + j]))
            if l < j:
                break
            sv += s[i + j]
    return 1

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
