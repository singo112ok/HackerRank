# https://www.hackerrank.com/challenges/angry-professor/problem

#속도를 개선할 방법이 있을법한데.. 일단 넘어갑니다
# 0이하의 값이 k값과 같아지면 no리턴 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    ArriveStd = 0
    for i in a:
        if i <= 0:
            ArriveStd += 1
            if ArriveStd >= k:
                return 'NO'
    return 'YES'




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()