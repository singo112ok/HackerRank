# https://www.hackerrank.com/challenges/the-power-sum/problem

# 이게되네?
# 우선 X 루트 N을 하면 어떤값을 N승했을 때 X보다는 작은 최대값을 구할 수 있음
# 만약 그 어떤값을 n승했을때 X와 같으면 0으로 떨어진것이므로 정답 수 증가 
# 0보다 크면 남은값으로 재귀함수를 돌리되 사용했던 값이 중복으로 사용되지 않게 MaxVal값을 세번째 파라미터로 넘겨줌
# 가장 하위까지 돌아 본 후 0으로 나눠 떨어진 카운트nAnswer값을 리턴
# 예전에 자판기 동전 잔돈주는거랑 풀 때와 거의 동일하게 푼거같다 당시엔 알맞지않는 방법이였으나 여기서 유도한방법은 맞는듯

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N, MaxVal):
    fRoot = X ** (1/N)
    nRoot = int(fRoot)
    if nRoot > MaxVal:
        nRoot = MaxVal

    nAnswer = 0
    
    for i in range(int(nRoot)):
        ResultVal = X - math.pow(nRoot-i, N)
        if ResultVal == 0:
            nAnswer += 1
            continue
        else: # ResultVal > 0:
            nAnswer += powerSum(ResultVal, N, nRoot-i-1)
    
    return nAnswer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    X = int(input())

    N = int(input())

    result = powerSum(X, N, X)

    fptr.write(str(result) + '\n')

    fptr.close()
