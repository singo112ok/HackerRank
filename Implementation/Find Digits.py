# https://www.hackerrank.com/challenges/find-digits/problem
# 문제 : 입력된 숫자의 각 자리수 값을 원래의 값과 나눠 나머지가 0이 되는 값의 수를 리턴
# 풀이 : 문자열로 나눈 뒤 0은 예외처리 나머지는 나머지가 0이면 카운트 증가

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    sN = str(n)
    nlen = len(sN)
    nCnt = 0
    for i in range(0, nlen):
        if sN[i] == '0':
            continue
        if n % int(sN[i]) == 0:
            nCnt += 1

    return nCnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
