# https://www.hackerrank.com/challenges/picking-numbers/problem

# 문제를 해석하면 기준값보다 절대값만큼 1 차이나는 값들로 서브 배열을 구해서 최대길이배열 값을 구하는건데
# 같거나+1로 구성된 배열, 같거나-1로 구성된 배열을 각각 구한 뒤 max값을 갱신시켜줌 재밌다

#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):    
    PlusList = []
    MinusList = []    
    ResultCnt = 0

    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] == a[j]:
                PlusList.append(a[j])
                MinusList.append(a[j])
            if a[i] == a[j]+1:
                PlusList.append(a[j])
            elif a[i] == a[j]-1:
                MinusList.append(a[j])
        if ResultCnt < len(PlusList):
            ResultCnt = len(PlusList)
        elif ResultCnt < len(MinusList):
            ResultCnt = len(MinusList)
        
        PlusList = []
        MinusList = []         

    return ResultCnt

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
