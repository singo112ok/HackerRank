# https://www.hackerrank.com/challenges/two-characters/problem

# 문제 : 2개의 문자만 남기고 모두 지웠을 경우 가장 긴 길이값을 가지는 문자열을 만들어라 그리고 그 문자열의 길이를 리턴하라
# 단 동일한 문자가 연속으로 위치하면 안된다
# 만들 수 없을경우 0  리턴

# 처음엔 연속으로 이어진 문자를 지우고 각 문자의 수를 카운트해서 합이 높은순으로 정렬해서 
# 다음 두 문자의 카운트 합보다 높거나 같은값이 나오면 그 값을 리턴시키고 종료하게 하려고 했으나 정렬이 쉽지 않음
# 모든 문자의 종류를 뽑아서 2개씩 다해볼 예정

# 난이도 easy
# 성공률 76.74%

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def checkCharCnt(s):

    Dic = {}
    while(len(s)!=0):
        cTemp = s[0]
        Dic[cTemp] = s.count(cTemp)
        s = s.replace(cTemp, '')

    return Dic

def DelContinueChar(s):
    bEnd = True

    while(bEnd):
        nLen = len(s)
        for i in range(0, nLen-1):
            if s[i] == s[i+1]:
                s = s.replace(s[i], '')
                break
            elif i == nLen-2:
                bEnd = False
                break
    return s          
 

def alternate(s):

    # print(checkCharCnt(s)) 사용안함 각 문자가 몇개씩 있나 확인해보는 용도

    # s = DelContinueChar(s) 연속된 문자 제거 기능 전처리로 이거부터 하면 속도개선이 될까 싶어 넣었는데 오히려 느려짐 타임아웃발생

    lCharlist = []
    sTemp = s
    nMaxCnt = 0
    
    while(len(sTemp)!=0):
        lCharlist.append(sTemp[0])        
        sTemp = sTemp.replace(sTemp[0], '')    

    for i in range(0, len(lCharlist)):      
        for j in range(i+1, len(lCharlist)):
            c1 = lCharlist[i]
            c2 = lCharlist[j]
            sTwochar = ''
            for k in range(0, len(s)):                
                if s[k] == c1:
                    sTwochar += c1
                elif s[k] == c2:
                    sTwochar += c2
                
                nTwoLen = len(sTwochar)
                
                if nTwoLen > 1:
                    if sTwochar[nTwoLen-2] == sTwochar[nTwoLen-1]:
                        sTwochar = ''
                        break
                
            if len(sTwochar) > nMaxCnt:
                nMaxCnt = len(sTwochar)

    if nMaxCnt < 2:
        nMaxCnt = 0            
    return nMaxCnt         




    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
