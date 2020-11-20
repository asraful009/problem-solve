#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    v = int(math.log(l^r, 2)) + 1
    c = (1<<(v))-1
    # print("{: >64} => {:0>64b}".format(r, r))
    # print("{: >64} => {:0>64b}".format(l, l))
    # print("{: >64} => {:0>64b}".format(l^r, l^r))
    # print("{: >64} => {:0>64b}".format(v, v))
    # print("{: >64} => {:0>64b}".format(c, c))
    return c
        
if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
