#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.
def theGreatXor(n):
    c = 0
    if n == 0:
        return 1
    for b in list('{0:0b}'.format(n)):
        print("{}".format(b), end="")
        if b == '0':
            c+=1
    v = 2**c -1
    print("\n{}".format(v))
    return v

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
