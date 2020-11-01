# https://www.hackerrank.com/challenges/tower-breakers-1/problem

# 어이없었던 문제 해독능력이 부족해서 처음엔 게임의 룰조차 이해하지 못하다가
# 자신을 제외한 약수가 a라면 층 수-a로 서로 층을 빼가면서 타워를 1층을 남겨 전달해주면
# 끝나는줄 알았는데 자신을 제외한 약수로 층 수를 줄여버리는거 였다
# 약수에 항상 1은 들어가므로 무조건 1로 만들어버리면 되니까 타워 개수에 따라 타워개수가 짝수면 2번이 승리
# 타워개수가 홀수면 1이 승리라고 조건을 줬더니 기본 예제빼고 모두 실패했다
# 그래서 테스트케이스 1번을 열어보니 100000 1, 100001 1 이 값이 2인게 있었다
# 층수가 1층이면 타워개수와 상관없이 무조건 2추가 승리하는거였다 그래서 해당 조건을 추가해주니 
# 모든 케이스 통과


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n, m):
    if m == 1:
        return 2    
    elif n%2 == 0:
        return 2
    else :
        return 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
