#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    m = max([ len(b) for b in "{:b}".format(n).split("0")])
    print(m)

