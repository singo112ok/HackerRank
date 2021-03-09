# https://www.hackerrank.com/challenges/counting-valleys/problem

# 이번에도 영문 해석이 쉽지않아서 예제보고 눈치로 이해했다..
#처음엔 등반의 수를 구했다가 틀린 예제보고 계곡의 수를 구하는거로 변경
# 0에서 -1로 가는 순간 == 계곡의 수와 같으니 시작과끝의 locate를 체크
#이제 몰아올리기 끝 앞으로 풀 때 마다 올릴 예정!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    nLocate = 0
    nValleyCnt = 0
    nZeroOne = [0,0]

    for i in range(0, n):
        if nLocate == 0: 
            nZeroOne[0] = 1        
        if s[i] == 'U':
            nLocate += 1
        else:
            nLocate -= 1        
        if nLocate == -1:
            nZeroOne[1] = 1         
        if sum(nZeroOne) == 2:
            nValleyCnt += 1

        # print(nLocate)
        # print(nValleyCnt)   
        nZeroOne[0] = 0
        nZeroOne[1] = 0       

    return nValleyCnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
