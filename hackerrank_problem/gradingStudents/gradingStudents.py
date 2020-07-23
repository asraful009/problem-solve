#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    newG = []
    for i in grades:
        m = -(-i // 5)
        nearVal = int(m) * int(5)
        print("{0} {1} {2}".format(i, nearVal, nearVal - i))
        if nearVal - i < 3 and nearVal >= 40:
            newG.append(nearVal)
        else :
            newG.append(i)
    #print(newG)
    return newG

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
