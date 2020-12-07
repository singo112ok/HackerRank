# https://www.hackerrank.com/challenges/camelcase/problem

# 단어가 몇개인지 찾기 첫 단어는 소문자 이후는 대문자
# 대문자 개수 +1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    sUpperChar = ''
    nLetCnt = 1

    for i in range(0, len(s)-1):
        sUpperChar = s[i+1].upper()
        if s[i+1] == sUpperChar:
            nLetCnt += 1

    return nLetCnt

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
