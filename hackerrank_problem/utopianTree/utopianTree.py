#!/bin/python3

import math
import os
import random
import re
import sys


tg = [0]*100

def c():
    i = 0
    tg[i] = 1
    i+=1
    while i<90:
        # a = 0
        if i % 2 == 1:
            tg[i] = tg[i-1] * 2
            # a = " * 2 "
        else:
            tg[i] = tg[i-1] + 1 
            # a = " + 1 "
        # print("{} {} {} => {}".format(i, tg[i-1], a, tg[i]))
        i+=1
    

def utopianTree(n):
    # print("{} {}".format(n, tg[n]))
    return tg[n]

if __name__ == '__main__':
    c()
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
