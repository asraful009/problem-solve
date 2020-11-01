#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # print("{} {} {}".format(a, k, queries))
    l = len(a)
    m = k % l
    # print("{} {}".format(l, m))
    
    arr = []
    for q in queries:
        # print("{} => a[{}] = {}".format(q, (l-m+q)%l, a[(l-m+q)%l]))
        arr.append(a[(l-m+q)%l])
    # print(i, a, arr)
    return arr

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)
    # for i in range(10):
    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
