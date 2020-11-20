#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    c = 0
    if n == 0:
        return 1
    for b in list('{0:0b}'.format(n)):
        # print("{}".format(b), end="")
        if b == '0':
            c+=1
    v = 2**c
    # print("\n{}".format(v))
    return v


if __name__ == '__main__':

    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
