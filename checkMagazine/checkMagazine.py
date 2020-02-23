#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print(magazine, note)
    for n in note:
        if n in magazine:
            # print("have", n, magazine)
            magazine.remove(n)
        else :
            # print("not", n, magazine)
            return "No"
        #print(n, i, magazine)
    return "Yes"

# Complete the checkMagazine function below.
def ckM(magazine, note):
    # print(magazine, note)
    M = {}
    N = {}
    for t in magazine:
        if t in M.keys() :
            M[t] += 1
        else :
            M[t] = 1
    l = 0
    for t in note:
        try:
            M[t] -= 1
            if M[t] < 0:
                return "No"
        except KeyError as identifier:
            return "No"
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    r = ckM(magazine, note)
    print(r)
