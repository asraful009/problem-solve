#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# def pickingNumbersWrong(a):
    
#     unqSet = []
#     dicSet = {}
#     for v in a:
#         if v not in unqSet:
#             unqSet.append(v)
#             dicSet[v] = 0
#         dicSet[v] += 1
#     unqSet.sort()
#     print("{} {} {}".format(a, dicSet, unqSet))
#     aa = []
#     # aa.append(unqSet[0])
#     l = len(unqSet)
#     i= 0
#     ele = 1
#     while i < l-1:
#         a = abs(unqSet[i] - unqSet[i+1])
#         if a <= 1:
#             if unqSet[i] not in aa:
#                 aa.append(unqSet[i])
#             if unqSet[i+1] not in aa:
#                 aa.append(unqSet[i+1])
#         print("qset[{}] => {} {} => {} // {}".format(i, unqSet[i], unqSet[i+1], a, aa))
#         i += 1

#     caountV = 0
#     for d in aa:
#         if caountV + dicSet[a] >= 5:
#             break
#         caountV += dicSet[a]
#     print("{}".format(caountV))
#     return ele

# def pickingNumbersnearest(a):
#     # a.sort()
#     print("a = {}".format(a))
#     l = len(a)
#     i = 0
#     pairSet = []
#     while i< l-1:
#         j = i+1
#         isAdded = False
#         while j < l:
#             print("a[{}] = {}, a[{}] = {}, {} => {}".format(i, a[i], j, a[j], pairSet, len(pairSet)))
#             print("=>>> abs +>{}".format(abs(a[i]-a[j])))
#             if abs(a[i]-a[j]) <= 1:
#                 # if len(pairSet) + 1 <= 5 :
#                 #     pairSet.append(a[i])
#                 if len(pairSet) + 1 <= 5 :
#                     pairSet.append(a[j])
#                     isAdded = True
#             j += 1
#         if isAdded == True:
#             if len(pairSet) + 1 <= 5 :
#                 pairSet.append(a[i])
#         i += 1

#     print("===>> {}".format(len(pairSet)))
#     return len(pairSet)

def pickingNumbers(a):
    a.sort()
    # print(a)
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
        # print("{}".format(t))
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
    # print("{} => {}".format(pickArr, maxv))
    return maxv

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
