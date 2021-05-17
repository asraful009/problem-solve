#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    print(q)
    a = []
    #[i for i in range(len(a)) if a[i] > 2]
    for i in range(len(q)):
        j = q[i] - i -1
        print(j)
        if(j>2) :
            print("Too chaotic")
            return
        if(j>0):
            a.append(j)
    
    print(sum(a))
    print("-------------------")

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
