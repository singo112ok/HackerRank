# https://www.hackerrank.com/challenges/insertionsort2/problem

# Easy Rate: 87.32

#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    for i in range(1, n):    
        nTempCnt = i+1
        
        for j in range(1, nTempCnt):
            if arr[nTempCnt-j] < arr[nTempCnt-j-1]:
                nSwap = arr[nTempCnt-j]
                arr[nTempCnt-j] = arr[nTempCnt-j-1]
                arr[nTempCnt-j-1] = nSwap
            else:
                break

        print(arr)
        
        





    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
