# https://www.hackerrank.com/challenges/a-very-big-sum/problem

# 파이썬은 변수형을 덜 신경 써도 되서 편했다

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in range(0, ar_count):
        sum = sum + ar[i]
    return sum    

if __name__ == '__main__':
    fptr = sys.stdout

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()