
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    l = len(c)
    i = 0
    # print(c, l)
    j = []
    j.append("-")
    while i < l-1:
        # print("{} {} {} {} {}".format(i, c[i], c[i+1], c[i+2], jump))
        if i+2 == l:
            i = i + 1
            j.append("-")
        elif c[i+2] == 1 :
            i = i + 1
            j.append("-")
        elif i+2 <= l:
            i = i + 2
            j.append("^")
            j.append("-")
        jump = jump + 1
        # print("jump : {} | {} / {}".format(jump, i, j))
    # print(jump)
    # print(j)
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
