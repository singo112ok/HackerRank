# https://www.hackerrank.com/challenges/counter-game/problem

# 비트연산을 어디다 쓰라는거지 싶어서 일단은 풀어봤다
# 2개통과 나머지 전부 타임아웃.. ㅎㅎ

#!/bin/python3

import math
import os
import random
import re
import sys
import math

# def counterGame(n):
#     nPos = 63  
#     bLouise = False

#     while True:
#         bLouise = not(bLouise)

#         for i in range(0, nPos):
#             nTemp = 2**(nPos-i)
#             if n > nTemp:
#                 n -= nTemp
#                 nPos = i
#                 break            
#             elif n == nTemp:
#                 n = (nPos-i)
#                 nPos = i
#                 break
        
#         if n == 1:
#             if bLouise == True:
#                 return 'Louise'
#             else:
#                 return 'Richard'        

# Complete the counterGame function below.
def counterGame(n):
    bLouise = False

    while True:
        bLouise = not(bLouise)
        nLen = len(bin(n))     
        sZero = '1'

        for i in range(nLen-3):
            sZero += '0' 

        sZero = '0b' +sZero     

        nTemp = int(sZero, 2)

        if n > nTemp:
            n -= nTemp
        elif n == nTemp:
            n = n//2
            
        if n == 1:
            if bLouise == True:
                return 'Louise'
            else:
                return 'Richard'              
      


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

