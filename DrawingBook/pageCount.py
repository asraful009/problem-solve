#!/bin/python3

import os
import sys

def pageCount(n, p):
    forw = p//2
    backw = (n//2) - forw
    # print(forw, backw)
    return forw if forw < backw else backw

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    # print("{}".format(result))
    fptr.write(str(result) + '\n')

    fptr.close()
