# https://www.hackerrank.com/challenges/circular-array-rotation/problem

#처음엔 로테이션 리스트를 구한 후 답을 뽑아내는 식으로 풀었는데 run time error를 timeout으로 잘못보고
# 동작시간을 줄이려고 queries만큼 반복하며 a에서 실제로 로테이션 된 값을 즉시 구해서 출력하는 방식으로 변경
# 회전을 2회이상 할 수 있다는 사실을 생각하지 않아서 4번 예제에서 run time error가 나는거였다(마이너스 인덱스에 접근)
# 해당 내용 수정 후 정상작동


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):    
    
    alen = len(a)
    ResultList = []
    lindex = 0
    for i in queries:
        lindex = i - k
        if lindex < 0:
            while lindex < 0:
                lindex += alen
        ResultList.append(a[lindex])   
    return ResultList

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
