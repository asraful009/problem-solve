#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c = 0
    isMount = False
    isValley = False
    countValley = 0
    for i in range(n):
        if s[i] == "U":
            if c == 0:
                isMount = True
                # print("M")
            c = c + 1
        else :
            if c == 0:
                isValley = True
                countValley = countValley + 1
                # print("V")
            c = c -1
        if c == 0:
            isMount = False
            isValley = False
            # print("-")
    print(countValley)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
