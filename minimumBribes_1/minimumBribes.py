#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    print(q)
    i = len(q)
    totalMove = 0
    move = 0
    while i => 0:
        x = q[i]
        j = i - 1
        move = 0
        while j >= 0 and q[j] > x:
            totalMove += 1
            move += 1
            q[j+1] = q[j]
            j -= 1
        q[j+1] = x
        i += 1
        print("localmove : {} {} {}".format(x, move, q))
    print(totalMove, q)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
