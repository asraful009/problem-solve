#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day = 13
    
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            day = 12
    elif year == 1918:
        day += 13
        # 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 - 14
    elif year >= 1919 and year <= 2700:
        # print("--- {} {} {}".format(year, year % 4 , year % 100))
        if year % 400 == 0:
            day = 12
        elif year % 4 == 0 and year % 100 != 0:
            day = 12

    y = "{}.09.{}".format(day, year)
    # print("{}".format(y))
    return "{}".format(y)

if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())
    # for i in range(1700, 1800):
    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
