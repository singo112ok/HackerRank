# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

# 힘들었던문제 처음엔 속도를 빠르게하려고 안태나 세울때마다 잘라넣기 하다가 오히려 그 속도가 오래 걸린건지 timeout까지도 발생했다
# 먼저 고정된 시작점(nBefore)에서 최대로 갈 수 있는 안테나 설치 위치를 찾고(nPos)
# 그 위치에서 어디까지 안태나가 영향을 줄 수 있는지(nAfter)를 찾아서 Antcnt를 올려주고
# 다시 시작점과 설치위치를 리셋 설치위치 혹은 영향을 줄 수 있는거리 측정시 최대거리를 넘지 않게 비교하여 (if nXlen ==)
# 최대치에 닿았으면 끝난것이므로 마지막 안태나 +1해주고 종료

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()
    nAntCnt = 0

    nPos = 0
    nBefore = 0
    nAfter = 1
    nXlen = len(x)

    if nXlen == 1:
        return 1

    while True:             
        if abs(x[nBefore] - x[nPos]) <= k:
            nPos += 1
            if nPos == nXlen:
                nAntCnt +=1                 
                return nAntCnt
            continue
        else:
            nAfter = nPos
            nPos -= 1
            
            while True:
                if abs(x[nAfter] - x[nPos]) <= k:
                    nAfter += 1                    
                    if nAfter == nXlen:                         
                        nAntCnt += 1       
                        return nAntCnt
                else:
                    nAntCnt += 1
                    nBefore = nAfter
                    nPos = nBefore                  
                    break                
    return nAntCnt            



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))
    
    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
