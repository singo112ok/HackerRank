# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# 이거도 예제보고 이해한 문제.. 
# 영어 찬찬히 읽어보자..

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    resultcnt = 0
    for i in range(0, n):
        for j in range(i+1, n):
            tempsum = ar[i] + ar[j]
            # print(tempsum)
            if tempsum % k == 0 :
                resultcnt += 1
    return resultcnt            


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()