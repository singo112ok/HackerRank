# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

# 구름위로 점프점프
# 예상했떤 예외케이스가 시작점 1일 때 그리고 에너지가 0이하 일때였는데
# 에너지가 0이하인 경우는 없었던거같고 시작점이 1일때는 예제 케이스에 딱 나타내줬다
# 실제 이동한 거리 nMove와 현재 배열속 위치 nPath값을 각각 두고 계산


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    nLife = 100
    nPath = 0
    nMove = 0
    nLenc = len(c)

    while True:
        nLife -= 1  #nLife <= 0 ?

        if c[nPath] == 1:
          nLife -= 2            

        nPath += k
        nMove += k

        if ((nMove%nLenc) == 0) :
            break
        if nPath >= nLenc:
            nPath -= nLenc

    return nLife



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
