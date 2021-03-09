#https://www.hackerrank.com/challenges/compare-the-triplets/problem

#list를 사용한 for문이 익숙하지 않을뿐

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ap = 0
    bp = 0
    for i in range(0,len(a)):
        if a[i] > b[i]:
            ap = ap+1
        elif b[i] > a[i]:
            bp = bp+1
    return [ap, bp]                   



if __name__ == '__main__':
    fptr = sys.stdout

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()