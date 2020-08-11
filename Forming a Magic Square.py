# https://www.hackerrank.com/challenges/magic-square-forming/problem

# 억지로 풀긴 풀었는데 많이 이상했던 문제
# 처음엔 3x3 magic square list가 5를중심으로 테두리만 돌아가는 4가지 케이스만 있는줄로 착각하였다 이후 8개인것을 알게 되었다
# 우선 이 3x3 magic square가 8개이며 그 정보를 알거나 magic square를 만드는 공식을 알아야만 풀 수 있는 문제다
# 뭐 여튼 8개값을 검색하여 가장 비교값이 적게 나오는것을 답으로 출력하였다

# 위 정보를 안다는 가정하에 단순 비교가 아닌 다른 방식으로 풀어보는법이 생각났는데
# 3x3 magic square의 테두리값은 2가지 케이스로 시계방향으로 고정이다 (예: [0][0], [0][1], [0][2], [1][2], [2][2], [2][1], [2][0], [1][0] 의 값은 시작점과
# 종료위치만 다를뿐 순서는 동일하다) 
# 심지어 그 2가지 케이스도 한가지 케이스의 미러버전 이므로
# 8 1 6 7 2 9 4 3
# 6 1 8 3 4 9 2 7
# 8가지 케이스 모두 비교하지 않고 해당값을 저 2케이스와 비교해보면 반복횟수를 줄일 수 있다 (8*9 => 8*2 + @)
# 물론 테두리 값을 뽑아 만드는게 소스도 보기 안좋아지고 더 걸릴 수 있을것 같다 


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    s = sum(s, [])

    ans = [[8, 1, 6, 3, 5, 7, 4, 9, 2]
    ,[6, 1, 8, 7, 5, 3, 2, 9, 4]
    ,[4, 3, 8, 9 ,5 ,1, 2, 7, 6]    
    ,[2, 7, 6, 9, 5, 1, 4, 3, 8]
    ,[2, 9, 4, 7, 5, 3, 6, 1, 8]
    ,[4, 9, 2, 3, 5, 7, 8, 1, 6]
    ,[6, 7, 2, 1, 5, 9, 8, 3, 4]
    ,[8, 3, 4, 1, 5, 9, 6, 7, 2]
    ]

    result = []
    sumval = 0
   
    # print(s)
    for i in range(8):
        for j in range(9):
            sumval += abs(s[j]-ans[i][j])
        if sumval == 0:
            return 0  

        result.append(sumval)
        sumval = 0
        
    # print(result)    
    return min(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
