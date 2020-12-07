#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    # print(p)
    a = []
    for i in range(len(p)):
        j = p.index(i+1)
        k = p.index(j+1)
        a.append(k+1)
        # print(f"{i+1} -> {j+1} -> {k+1}")
    # print(a)
    return a

if __name__ == '__main__':
    fptr = open("./o.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
