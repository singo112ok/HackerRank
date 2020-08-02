#https://www.hackerrank.com/challenges/mini-max-sum/problem

# python의 list는 너무 편리한거 같다 영상처리 같은 실시간 처리가 아니라면 C에서도
# 링크드리스트를 쓰는게 좋지않을까?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    tempsum = [0, 0, 0, 0, 0]
    i = 0
    j = 0

    for i in range(0, len(arr)) :
        for j in range(0,len(arr)):
            if j == i :
                continue
            tempsum[i] = tempsum[i]+ arr[j]
    
    print(min(tempsum) , end='')
    print(" ",  end='')
    print(max(tempsum)) 
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)