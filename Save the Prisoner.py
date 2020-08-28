# https://www.hackerrank.com/challenges/save-the-prisoner/problem

#!/bin/python3

# 조금재밌었다 근데 죄수들에게 이런장난을 쳐도 되는건가..? ㅠㅠ
# 우선 사탕에서 죄수를 나눈 나머지로 마지막 루프 상태를 만들고
# 시작점(s)를 더해주되 시작점도 먹어야하니 -1해줘서 임시로 마지막 먹는사람을 구함 (nResult)
# 그러나 이 값은 시작점과 남은 사탕에 따라 한바퀴를 초과 시킬수도 혹은 0이되면 역으로 마이너스가 될 수 있으므로
# 해당 값이 0이하거나 값을 초과한경우 회전을 시켜 위치를 찾아준다

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    
    m = m%n    
    nResult = m+s-1
    if nResult <= 0:
        nResult += n
    if nResult > n:
        nResult -= n

    return nResult
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
