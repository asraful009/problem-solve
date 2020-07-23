#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def ckMode(a, i):
    # print("{} {}".format(a, i))
    if(a<i) :
        return i%a == 0
    else :
        return a%i == 0


def getTotalX(a, b):
    #return "{} {}".format(a, b)
    minA = min(a)
    maxA = max(a)

    minB = min(b)
    maxB = max(b)

    #print("A :[{} {}], B: [{} {}]".format(minA, maxA, minB, maxB))
    out = []
    for i in range(maxA, minB+1):
        outCK = [ckMode(ax, i) for ax in a+b]
        #print("{} : {} {}".format(outCK, any(outCK), i))
        if all(outCK):
            out.append(i)
    # print("{}".format(out))

    return len(out)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("./r/output/my.txt", 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
