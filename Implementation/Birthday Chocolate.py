# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# 너무 간단한 이중포문.. 생각도 별로 안하고 바로 한거같다


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    AnsCnt = 0
    
    for i in range(0, len(s)+1-m):
        tempSum = 0    
        for j in range(0, m):
            tempSum += s[i+j]
        # print(tempSum)    
        if tempSum == d:
            AnsCnt += 1            
    return AnsCnt             




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()