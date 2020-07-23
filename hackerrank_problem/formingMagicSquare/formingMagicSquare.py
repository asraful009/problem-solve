#!/bin/python3

import math
import os
import random
import re
import sys


def printM(mat):
    print("- - -")
    for i in mat:
        for j in i:
            print("{} ".format(j), end = '')
        print("")
    print("- - -")

def matRot(mat):
    tm = []
    for i in range(0, 3):
        new = []
        for j in range(0, 3):
            new.append(mat[i][j])
        tm.append(new)
    

    mat[0][0] = tm[0][1]
    mat[0][1] = tm[0][2]
    mat[0][2] = tm[1][2]

    mat[1][0] = tm[0][0]
    mat[1][1] = tm[1][1]
    mat[1][2] = tm[2][2]

    mat[2][0] = tm[1][0]
    mat[2][1] = tm[2][0]
    mat[2][2] = tm[2][1]

    return mat


def matRotMirrLR(mat):
    tm = []
    for i in range(0, 3):
        new = []
        for j in range(0, 3):
            new.append(mat[i][j])
        tm.append(new)
    

    mat[0][0] = tm[0][2]
    mat[0][1] = tm[0][1]
    mat[0][2] = tm[0][0]

    mat[1][0] = tm[1][2]
    mat[1][1] = tm[1][1]
    mat[1][2] = tm[1][0]

    mat[2][0] = tm[2][2]
    mat[2][1] = tm[2][1]
    mat[2][2] = tm[2][0]

    return mat

def matRotMirrTB(mat):
    tm = []
    for i in range(0, 3):
        new = []
        for j in range(0, 3):
            new.append(mat[i][j])
        tm.append(new)
    

    mat[0][0] = tm[2][0]
    mat[0][1] = tm[2][1]
    mat[0][2] = tm[2][2]

    mat[1][0] = tm[1][0]
    mat[1][1] = tm[1][1]
    mat[1][2] = tm[1][2]

    mat[2][0] = tm[0][0]
    mat[2][1] = tm[0][1]
    mat[2][2] = tm[0][2]

    return mat

def matRotDia(mat):
    tm = []
    for i in range(0, 3):
        new = []
        for j in range(0, 3):
            new.append(mat[i][j])
        tm.append(new)
    

    mat[0][0] = tm[0][0]
    mat[0][1] = tm[1][0]
    mat[0][2] = tm[2][0]

    mat[1][0] = tm[0][1]
    mat[1][1] = tm[1][1]
    mat[1][2] = tm[2][1]

    mat[2][0] = tm[0][2]
    mat[2][1] = tm[1][2]
    mat[2][2] = tm[2][2]

    return mat

def calcMin(a, b):
    # print("-------------")
    # printM(a)
    # printM(b)
    
    m = 0
    for i in range(0, 3):
        for j in range(0, 3):
            m += abs(a[i][j] - b[i][j])
    # print("m = {}".format(m))
    # print("-------------")
    return m

# Complete the formingMagicSquare function below.
def formingMagicSquare(a):
    aa = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
    minArr = []
    minV = 1000
    for s in pre:

        minArr.append(calcMin(s, a))
        # minArr.append(calcMin(s, matRotDia(a)))

        # minArr.append(calcMin(s, matRotMirrTB(a)))
        # minArr.append(calcMin(s, matRotMirrTB(matRotDia(a))))

        # minArr.append(calcMin(s, matRotMirrLR(a)))
        # minArr.append(calcMin(s, matRotMirrLR(matRotDia(a))))

        # minArr.append(calcMin(s, matRotMirrLR(matRotMirrTB(a))))
        # minArr.append(calcMin(s, matRotMirrLR(matRotMirrTB(matRotDia(a)))))

    print("{} => {}".format(minArr, min(minArr)))
    


        # a = matRot(a)
        # for i in range(1, 10):
        #     a = matRot(a)
        #     printM(s)
        #     v = calcMin(a, s)
        #     print("{}".format(v))
        #     if(minV > v):
        #         minV = v
        # print("{}".format(minV))
    return min(minArr)


if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')

    fptr.close()
