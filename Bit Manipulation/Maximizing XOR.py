# https://www.hackerrank.com/challenges/maximizing-xor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    nMaxVal = 0
    for i in range(l, r):
        # for j in range(i, r-i+l+1):
        for j in range(i,r):
            if i^j > nMaxVal:
                nMaxVal = i^j
    return nMaxVal




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
