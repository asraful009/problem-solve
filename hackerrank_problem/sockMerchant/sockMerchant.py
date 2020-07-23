
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    a = {}
    for i in ar:
        if i not in a:
            a[i] = 0
        a[i] = a[i] + 1
    # print(a)
    s = 0
    for i in a:
        # print("{} {} < {} {} {}".format(float(a[i]), float(a[i] // 2) , float(a[i] / 2), float(a[i] // 2)*2 , float(a[i] / 2)*2))
        s = s + int(float(a[i] // 2))
    # print(s)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()

