# https://www.hackerrank.com/challenges/migratory-birds/problem

# 종류별 수만큼 카운트해놓고 최대값 어렵지 않았다

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    cnt = []
    resultVal = 0

    for i in range(0, 5):
        cnt.append(arr.count(i+1))
    
    # print(cnt)
    nMax = max(cnt)
    # print(nMax)

    for i in range(0, 5):
        if cnt[i] == nMax:
            resultVal = i+1
            break

    return resultVal 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
