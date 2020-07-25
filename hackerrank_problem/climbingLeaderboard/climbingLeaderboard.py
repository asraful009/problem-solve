#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard_solve_but_slow(scores, alice):
    # v = []
    # for s in scores:
    #     if s not in v:
    #         v.append(s)
    
    # # for s in alice:
    # #     if s not in v:
    # #         v.append(s)
    # v.sort(reverse=True)
    v = list(dict.fromkeys(scores))
    # print("{}".format(v))
    l = len(alice)
    k = len(v)
    i = 0
    pos = [] #[1] * l

    while i < l:
        j=0
        while j<k:
            # print("[{}] = {} >= [{}] = {}".format(i, alice[i], j, v[j]))
            if alice[i] >= v[j]:
                break
            j +=1
        pos.append(j+1)
        i += 1
    print("{} {} {}".format(v, alice, pos))
    return pos



# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    smax = sys.maxsize
    smin = -sys.maxsize - 1
    scores = [smax] + scores
    scores.append(smin)
    v = list(dict.fromkeys(scores))
    print(v)
    l = len(alice)
    k = len(v)
    i = 0
    pos = []
    while i < l:
        T = alice[i]
        L = 0
        R = k-1
        while L != R:
            m = math.ceil((L + R) / 2)
            if v[m] > T:
                L = m
            else:
                R = m - 1
            if v[L] == T:
                break
        pos.append(L+1)
        i+=1
    # print("{} {} {}".format(v, alice, pos))
    return pos

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
