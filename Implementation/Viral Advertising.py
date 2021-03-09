# https://www.hackerrank.com/challenges/strange-advertising/problem
#!/bin/python3

# 공식이 이미 문제에 다 있어서 따라 만들면 된다..

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    nSum = 2
    link = 2
    Shared = 0

    if n == 1:
        return 2

    for i in range(0, n-1):
        Shared = (link*3)
        link = int(Shared/2)
        nSum += link
    
    return nSum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr = sys.stdout

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
