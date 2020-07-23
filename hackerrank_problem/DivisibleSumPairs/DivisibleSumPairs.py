#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    # print("{} {} {}".format(n, k, ar))
    l = len(ar)
    t = 0
    for i in range(0, l):
        for j in range(i+1, l):
            s = ar[i]+ar[j]
            if s%k == 0:
                t+=1
            # print("( ar[{}] = {} , ar[{}] = {} ) => {} -> {} >> {}".format(i, ar[i], j, ar[j], s, (s%k), t ))
    return t

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
