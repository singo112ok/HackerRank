# https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=next-challenge&h_v=zen

#삽입정렬1 
#문제 : 정렬되어있는 배열에서 가장마지막 인덱스에 특정값을 추가하고 그 값이
# 삽입정렬로 자리를 찾아가는 과정을 출력하라(단 매번 스왑하는 방식이 아니라  맨마지막 값은 가장마지막에 값이 입력됨)

# Easy Rate: 87.32

#!/bin/python3

import math
import os
import random
import re
import sys

def printList(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')
        print(' ', end='')    
    print('')


def insertionSort1(n, arr):
    nVal = arr[n-1]
    for i in range(2, n+1):
        if nVal < arr[n-i]:
            arr[n-i+1] = arr[n-i]
            printList(arr)
        else:            
            arr[n-i+1] = nVal
            printList(arr)
            return 0   
    arr[0] = nVal
    printList(arr)
    return 0       
    
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
