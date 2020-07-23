#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarrayw(a):
    # a.sort()
    print(a)
    pickArr = []
    i = 0
    while len(a) !=0 :
        i = 0
        t = a[i]
        del a[i]
        tempPick = []
        tempPick.append(t)
        l = len(a)
        j = 0
        print("{}".format(t))
        while j< l:
            if abs(t - a[j]) <= 1 : #and len(tempPick) + 1 <= 5:
                tempPick.append(a[j])
            j += 1
        # if len(tempPick) > 1:
        pickArr.append(tempPick)
        i += 1
    maxv = max([len(m) for m in pickArr ])
    if maxv == 1:
        maxv = 0
    print("{} => {}".format(pickArr, maxv))
    return 1


def longestSubarray(arr):
    # print(arr)
    l = len(arr)
    if l == 1:
        return 1
    i = 0
    pickArr = []
    temp = []

    while i < l-1:
        j = i+1
        temp = []
        temp.append(arr[i])
        while j < l:
            # print("{} {} {}".format(arr[i], arr[j], abs(arr[i] - arr[j])))
            if abs(arr[i] - arr[j]) <= 1:
                temp.append(arr[j])
            else :
                break
            j += 1
        pickArr.append(temp)
        # print("{}".format(temp))
        i += 1
    
    maxv = max([len(m) for m in pickArr ])
    # print("{}".format(pickArr))
    
    # print("{} => {}".format(pickArr, maxv))
    return maxv

if __name__ == '__main__':
    fptr = open(".my.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
