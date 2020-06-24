#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a = {}
    minMax = 0
    key = arr[0]
    for i in arr:
        if str(i) in a:
            a[str(i)] += 1
        else :
            a[str(i)] = 1
        # print("a[{}] = {}".format(i, a[str(i)]))
    for k, v in a.items():
        if minMax < v and key < int(k):
            minMax = v
            key = int(k)
        # print("{} => {} [{} {}]".format(k, v, key, minMax))
    # print("{} {}".format(key, minMax))
    return key

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
