#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b):
    v = a
    c = b^a
    nV = 2**int(math.log(c, 2)) - 1
    vv = a & ~nV
    # print("{:0>64} => {:0>64b}".format(b,b))
    # print("{:0>64} => {:0>64b}".format(a, a))
    # print("{:0>64} => {:0>64b}".format(c, c))
    # print("{:0>64} => {:0>64b}".format(nV, nV))
    # print("{:0>64} => {:0>64b}".format(vv, vv))
    # for i in range(a, b+1):
    #     print("{0:b}".format(i).rjust(32, '0'))
    #     # v&=i
    # print(v, c)
    return vv
    
if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()