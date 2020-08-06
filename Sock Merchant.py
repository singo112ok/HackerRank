# https://www.hackerrank.com/challenges/sock-merchant/problem

# 리스트를 이용하여 종류별로 카운트를 세고
# 2로 나눈 몫으로 쌍의 수를 구했다 어렵진 않았으나 
# 더 쉽게 할 방법도 있지 않았을까 싶었던 문제

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    arType = list(set(ar));
    arType.sort()

    # lCount = [0 for i in range(n)]
    lCount = [0]*len(arType)   
    lresult= []

    for i in ar:
        for j in range(0, len(arType)):
            if i == arType[j]:
                lCount[j] = lCount[j] + 1;
    
    # print(arType)                
    # print(lCount)
    for i in lCount:
        lresult.append(int(i/2))
    
    # print(lresult)    
    return sum(lresult) 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
