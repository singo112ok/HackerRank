# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

#!/bin/python3

#처음 공식을 세웠을 때 열에서 뒤집었을 떄 가장 큰 이득을 볼 수 있는라인을 1회 뒤집고
# 행에서 뒤집었을 때 가장 큰 이득을 보는 라인을 1회뒤집고
# 열 행 열 행 식으로 반복하다가 더이상 뒤집을게 없으면 합을 계산하여
# 종료 하는식으로 풀었고 예제 두개는 통과하였으나 다른 모든 문제에 타임아웃이 걸렸다
# 도저히 못풀겠어서 답을 찾아보니 아래와 함수와 같이 간단하게 풀이되었는데 해석해보면
# 배열기준 0열 0행의 위치의 값은 n-1열 n-1행, 0열 n-1행, n-1열 0행 단 4곳밖에 이동 할 수 없다
# 즉 이동가능한 위치의 값들 중 가장 큰값을 사용하게 될 거라는것인데
# 그로인해 matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1]
# 위 4개의 값 중 가장 큰 값을 누적합 시켜서 계산하는것이였다
# 비슷한 유형을 경험해보지않고는 풀지 못했을 것 같다



import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

def flipping(matrix, nLen, bCol, nCnt): # 뒤집기
    if bCol == True:
        for i in range(int(nLen/2)):
            nTemp = matrix[i][nCnt]
            matrix[i][nCnt] = matrix[nLen-i-1][nCnt]
            matrix[nLen-i-1][nCnt] = nTemp
  
    else:
        for i in range(int(nLen/2)):
            nTemp = matrix[nCnt][i]
            matrix[nCnt][i] = matrix[nCnt][nLen-i-1]
            matrix[nCnt][nLen-i-1] = nTemp                  
    
    return matrix

def flippingMatrix2(matrix):
    nLen = len(matrix)    

    while(True):        
        bClearC = True
        bClearR = True
        lMax = [0,0]        
       
        for i in range(nLen):            
            nSum = 0
            for j in range(nLen):                
                if j < nLen/2:
                    nSum += matrix[j][i]                    
                else:
                    nSum -= matrix[j][i] 
            if nSum < lMax[0]:
                lMax[0] = nSum
                lMax[1] = i
                bClearC = False
        
        if bClearC == False:
            flipping(matrix, nLen, True, lMax[1])

        lMax = [0,0]
        for i in range(nLen):   
            nSum = 0        
            for j in range(nLen):
                if j < nLen/2:
                    nSum += matrix[i][j]                    
                else:
                    nSum -= matrix[i][j] 
            if nSum < lMax[0]:
                lMax[0] = nSum
                lMax[1] = i
                bClearR = False                

        if bClearR == False:
            flipping(matrix, nLen, False, lMax[1])                

        if (bClearC and bClearR):
            nSumVal = 0
            for i in range(int(nLen/2)): 
                for j in range(int(nLen/2)):
                    nSumVal += matrix[i][j]
            return nSumVal



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
