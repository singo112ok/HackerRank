# https://www.hackerrank.com/challenges/between-two-sets/problem

# 영문 리딩능력이 부족해서 문제가 이해안가서 고생한 문제 ㅠㅠ
# 살짝만 문장을 잘못 번역해도 전혀 다른값을 구하게 되고 심지어 
# 내가 구한 다른값들이 테스트케이스의 80퍼를 통과해서 알고리즘에 예외케이스인줄 알고 시간 많이 썼다..
# 이번기회에 리딩연습 하자...

import math
import os
import random
import re
import sys

# 1 1
# 1
# 100

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
       if greater > 100 :
        return -1

   return lcm


def getTotalX(a, b):
   
    nLem = 1
    lLem = []
    nResultCnt = 0
    nCheckCnt = 0
    nRoop = 1    

    for i in a:
        nLem = compute_lcm(nLem, i)
        if nLem == -1:
            return 0

    nInputVal = nLem        
    while nInputVal <= b[0] :       
        lLem.append(nInputVal)
        nRoop = nRoop +1        
        nInputVal = nLem * nRoop

    print(lLem)      
    for i in lLem :
        for j in b :        
            if j%i != 0:              
                break
            else:
                nCheckCnt = nCheckCnt+1
        if nCheckCnt == len(b) :
            nResultCnt = nResultCnt+1
        nCheckCnt = 0    
    return nResultCnt      

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
