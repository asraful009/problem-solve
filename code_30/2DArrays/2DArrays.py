#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    v = []
    for k in range(4):
        for i in range(4):
            v.append(
                  arr[k][i+0] + arr[k][i+1] + arr[k][i+2]
                + arr[k+1][i+1]
                + arr[k+2][i+0] + arr[k+2][i+1] + arr[k+2][i+2]
            )
    print(max(v))