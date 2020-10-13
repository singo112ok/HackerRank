# https://www.hackerrank.com/challenges/lonely-integer/problem

# 오름차순으로 정렬 후 현재위치와 이전위치 값 비교
# 같으면 둘다 삭제 후 다시 처음부터 비교
# 계속 지우다보면 결국 길이가 1이 되고 해당값 출력
# ----------------------------------------



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
# def lonelyinteger_old(a):
#     a.sort()
#     nIndex = 0

#     while True:
#         nIndex += 1

#         nLenA = len(a) 
#         if nLenA == 1:
#             return a[0] 

#         if a[nIndex] == a[nIndex-1]:
#             del a[nIndex]
#             del a[nIndex-1]
#             nIndex = 0
#             continue        

def lonelyinteger(a):
    result = 0

    for i in a:
        result = result ^ i
    return result


        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
