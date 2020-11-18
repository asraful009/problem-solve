#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    v = {}
    for i in a:
        if i not in v:
            v[i] = 0
        v[i] += 1
    # print(v)
    r = -1
    for k in v:
        if(v[k] == 1 ):
            r = k
            break
    # print(r)
    return r


if __name__ == '__main__':
    fptr = open("./my.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
