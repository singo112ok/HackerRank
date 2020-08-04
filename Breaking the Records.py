# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# 문제 난이도가 갑자기 너무 내려가서 당황..

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxScore=scores[0]
    minScore=scores[0]
    maxCnt = 0
    minCnt = 0

    for i in scores:
        if i > maxScore:
            maxScore = i
            maxCnt = maxCnt + 1
        elif i < minScore:
            minScore = i
            minCnt = minCnt + 1
    return [maxCnt, minCnt]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()