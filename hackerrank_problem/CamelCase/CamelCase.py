#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    l = len(re.findall('^[a-z]+|[A-Z][^A-Z]*', s))
    print(l)
    return l

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
