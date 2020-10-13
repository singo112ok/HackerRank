# https://www.hackerrank.com/challenges/maximizing-xor/problem

#!/bin/python3

# 간만에 쉬운거푸니 속이 다 편안하다
# 이거도 무슨 공식이 있을까 이중포문돌리면 타임아웃나지 않을까
# 노심초사했는데 일단 패스 ㅎㅎ


import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    nMaxVal = 0
    for i in range(l, r+1):
        for j in range(i,r+1):
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
