#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    # print(n)
    """
    d1[5,0] :  5/2 = 2 =>2*3 = 6    -> 0 + 2
    d2[6,2] :  6/2 = 3 =>3*3 = 9    -> 2 + 3
    d2[9,5] :  9/2 = 4 =>4*3 = 12   -> 5 + 4
    d2[12, 9]: 12/2 = 6 =>6*3 = 18  -> 9 + 6 
    ...
    """
    cul = 0
    t = 5
    for i in range(n):
        nCul = int(t/2)
        cul += nCul
        t = 3 * nCul
        # print(
        #     "[{}] :  {}, {} => {}"
        #     .format(i, t, cul, nCul))
    
    print(cul)
    return cul

if __name__ == '__main__':
    fptr = open("./output/my.txt", 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
