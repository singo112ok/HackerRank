# https://www.hackerrank.com/challenges/permutation-equation/problem

#해커랭크 4레벨 달성~
#문제는 그냥 쉬웠던 문제 위치 찾기를 두번 돌렸다 만약 두번을 초과 했다면
#따로 함수로 만들었을듯

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    pList = []
    rList = []

    for i in range(1, len(p)+1):
        pList.append(p.index(i)+1)

    for j in pList:
        rList.append(p.index(j)+1)        
    
    return rList


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
