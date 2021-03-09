# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

# 숫자 뒤집는 함수 별도로 만들고 나누기를 완료 한 값이 
# 소숫점이 있는지 확인하기위해 int형변환 한거에서 자신을 뺐을때 0 이면 카운트 추가 

#!/bin/python3

import math
import os
import random
import re
import sys

def reverseNum(iVar):
    sTemp = str(iVar)
    sResult = ''
    for i in range(0, len(sTemp)):
        sResult += sTemp[len(sTemp)-1-i]
    return int(sResult)

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    nResultCnt = 0
    nTemp = 0

    for roop in range(0, j-i+1):
        nTemp = (i+roop) - reverseNum(i+roop)
        if nTemp < 0:
            nTemp *= -1
        nTemp /= k
        if int(nTemp) - nTemp == 0 :
            nResultCnt += 1
    
    return nResultCnt        


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
