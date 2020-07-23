#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = sum(bill)
    s -= bill[k]
    s //= 2
    if(s == b):
        print("Bon Appetit")
    else :
        # print("{} {} {}".format(s, b, abs(s-b)))
        print("{}".format(abs(s-b)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
