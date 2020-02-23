
import datetime
import os
import sys


def timeConversion(s):
    dt = datetime.datetime.strptime(s, "%I:%M:%S%p")
    s = dt.strftime("%H:%M:%S")
    #print(s)
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
