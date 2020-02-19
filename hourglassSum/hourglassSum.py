#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = float("-inf")
    for i in range(4):
        for j in range(4):
            # print("M : {} {} ".format(i, j))
            s = 0
            for k in range(3):
                for l in range(3):
                    s += arr[i+k][j+l]
                    # print("[{}, {}] {}/{} ".format(k+i, l+j, arr[i+k][j+l], s), end= "")
                # print("")
            # print("{} += - [{}, {}] {} - [{}, {}] {}".format(s, i+1, j, arr[i+1][j], i+1, j+2, arr[i+1][j+2]))
            s += - (arr[i+1][j] + arr[i+1][j+2])
            # print(s)
            if max < s :
                max = s

    # print(max)
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
