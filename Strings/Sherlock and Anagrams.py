# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem


#  level : medium, Success Rate : 87.92%

# 문제 : 주어진 문자열에서 에너그램인 하위문자열이 몇쌍인지 구하시오

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    tempStr1 : str = ''
    tempStr2 : str = ''  
    count : int = 0
    lenS : int = len(s)

    #한글자씩 탐색, 두글자씩 탐색 , 3개씩 탐색 루프를 만들어야함 3중루프여야할듯
    for strlen in range(1, lenS+1):  #글자 길이 수 
        for i in range(0, lenS-strlen):     #앞문자 시작위치
            for j in range(i+1, lenS-strlen+1): #뒷 문자 시작위치
                tempStr1 = s[i:i+strlen]              
                tempStr2 = s[j:j+strlen]
                if sorted(tempSet1) == sorted(tempSet2):
                    print(tempSet1, tempSet2)
                    count+=1              
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
