# https://www.hackerrank.com/challenges/strong-password/problem

# 강력한 암호 규정을 통과하기 위해 추가해야하는 char 수
# 문자하나씩 조건 체크, 최소 필요한 길이와 조건수 비교하여 더 큰값 리턴

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    minVal = 0

   
    if 6 > n:
        minVal = 6-n
    
    checkNum = 0
    checkLow = 0
    checkUp = 0
    checkSC = 0

    for i in range(0, n):
        cnt = 0
        if checkNum == 0:
            if numbers.find(password[i]) >= 0:
                checkNum = 1
                continue
        
        if checkLow == 0:
            if lower_case.find(password[i]) >= 0:
                checkLow = 1
                continue

        if checkUp == 0:
            if upper_case.find(password[i]) >= 0:
                checkUp = 1
                continue

        if checkSC == 0:
            if special_characters.find(password[i]) >= 0:
                checkSC = 1
                continue            
    
    nSum = checkNum + checkLow + checkUp + checkSC

    if nSum == 4:
        return minVal 
    else:
        if minVal > 4-nSum:
            return minVal
        else:
            return 4-nSum              


    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
