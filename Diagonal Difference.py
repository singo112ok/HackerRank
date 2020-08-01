# https://www.hackerrank.com/challenges/diagonal-difference/problem

# 샘플 데이터로 공식을 짜놓고 i, i 의 합 i, n-i-1 의 합을 그대로 구현

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    ltor = 0
    rtol = 0
    result = 0
    for i in range(0, n):
        ltor = ltor + arr[i][i]
        rtol = rtol + arr[i][n-i-1]
    result = ltor - rtol
    if result < 0:
        result = result * -1

    return result    
        

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()