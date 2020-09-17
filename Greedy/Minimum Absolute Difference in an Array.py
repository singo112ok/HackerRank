# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

# 이중 포문 돌리면서 최소값 찾는작업 진행하니 2번,3번 케이스가 타임아웃 발생
# list의 중복값을 제거 후 돌려도 동일함 중복값이 없는듯

# 최소값 비교횟수라도 줄이려고 차이 값을 리스트에넣고 
# 루프돌때 마다 리스트의 최소값을 뽑아서 비교해보았으니 타임아웃 늘어남
# 싹다 리스트에 넣으니 런타임에러뜸... 리스트에 최대치가있나?
# ---- 해결----
# sort를 시켜놓고 자기 우측과만 비교하면 된다 허 참 ㅡ.ㅡ;;
# 포문이 한번돈다


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    
    minval = int(10e9)

    arr.sort()
    Alen = len(arr)

    for i in range(0, Alen-1):
        if minval > arr[i+1] - arr[i]:
            minval = arr[i+1] - arr[i]

    return minval





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
