#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    # print("{} {}".format(k, a))
    m = 0
    for i in a:
        if i <= 0:
            m +=1
    # print("{}".format(m))
    s = "NO"
    if m < k:
        s = "YES"
    # print(s)
    return s

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
