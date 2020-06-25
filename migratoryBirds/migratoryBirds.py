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
    # print("{}".format(a))
    minMax = a[str(key)]
    for k, v in a.items():
        # print("k:{} => v:{} [key:{} mm:{}] {} and {}".format(k, v, key, minMax, minMax <= v, int(k) < int(key)))
        if minMax < v:
            minMax = v
            key = int(k)
            # print("-----> k:{} => v:{} [key:{} mm:{}]".format(k, v, key, minMax))
        elif minMax == v and int(k) < int(key):
            minMax = v
            key = int(k)
            # print("-----> k:{} => v:{} [key:{} mm:{}]".format(k, v, key, minMax))
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
