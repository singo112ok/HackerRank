# https://www.hackerrank.com/challenges/reduced-string/problem

# 첫 string문제 파이썬은 변수타입이 없기에 리스트로 변형해서 작업
# 문자열의 길이가 2이상인 경우 연결된 문자가 동일하면
# 잘라서 다시 넣고 루프를 반복하는작업 문자열 탐색을 끝까지 마쳤는데도 
# 리셋작업이 없었다면 리턴

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    while True:
        if len(s) == 0:
            return 'Empty String'
        elif len(s) == 1:
            return s        

        sBefore = s[0]
        nEsc = 0


        for i in range(0, len(s)-1):
            if sBefore == s[i+1]:
                if i >= 1:
                    s = s[:i] + s[i+2:]
                else:
                    s = s[i+2:]
                nEsc = 1   
                break;
            else:
                sBefore = s[i+1]
        
        if nEsc == 0:
            return s




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
