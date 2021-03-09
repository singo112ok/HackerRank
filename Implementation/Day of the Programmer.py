# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#대충 윤달은 4년에 한번온다 그래서 생일이 4년에 한번인 사람도 있다정도
#알고있었는데 줄리안 그레고리 이러면서 위키링크에 더 헷갈렸다
#국가도 위키링크와 달라서.. 사수가 본문이 헷갈렸다하여 대충들은 기억에
#패스하지못하는 케이스까지 포인트로 풀어가며 했다..

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    nGregorian = 0
    resultval = ''

    if year == 1918:
        nGregorian = 2
    elif year < 1918:
        if year%4 == 0:
            nGregorian = 1
    else: 
        if year%400 == 0:
            nGregorian = 1
        elif (year%4==0) and (year%100!=0):
            nGregorian = 1

    if nGregorian == 1:
        resultval = '12.09.' + str(year)  
    elif nGregorian == 2:
        resultval = '26.09.' + str(year)           
    else:
        resultval = '13.09.' + str(year)   
    return resultval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
