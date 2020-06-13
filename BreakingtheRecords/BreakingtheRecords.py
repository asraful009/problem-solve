#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    vMax = scores[0]
    vMin = scores[0]
    cMax = 0
    cMin = 0
    for i in scores:
        if vMax < i:
            cMax += 1
            vMax = i
        if vMin > i:
            cMin += 1
            vMin = i
        #print("{} [{}:{}]/[{}:{}]".format(i, vMax, cMax, vMin, cMin))
    #print("{} {}".format(cMax, cMin))
    return [cMax, cMin]

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
