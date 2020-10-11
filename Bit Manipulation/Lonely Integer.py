# https://www.hackerrank.com/challenges/lonely-integer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    a.sort()
    nIndex = 0

    while True:
        nIndex += 1

        nLenA = len(a) 
        if nLenA == 1:
            return a[0] 

        if a[nIndex] == a[nIndex-1]:
            del a[nIndex]
            del a[nIndex-1]
            nIndex = 0
            continue        
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
