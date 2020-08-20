# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# 포기할 뻔 했던 문제
# 처음에 문제읽고 이게 왜 미디움에 통과률이 50퍼대일까 싶었는데
# 케이스 4가지가 타임아웃이 났다
# 이 방법 써보고 저 방법써봐도 4가지 케이스에서 타임아웃을 벗어 날 수 없었고
# 파이썬이라 느려서 이러나 싶기도하고
# 2일동안 매달렸다가 힌트라도 얻어보려고 disscussions에 들어갔으나
# 파이썬으로 푼 사람들은 다 일반적이지 않은(약간 편법적인) 방법을 써서 
# (특정값이 어디 사이값인지 위치를 찾아주는 함수사용 , 기존 코드 없애고 애초에 map으로 받으며 처리)
# 처리하고 있었다 현재 사수와 스터디로 함께 풀고 리뷰하는데 사수해당 문제를 풀었는데 
# 정렬 후 검사한부분은 제거해서 배열을 재정의해 검색속도를 올리는 방법으로 풀었다고 하였다
# 그런데 그것도 for문으로 했을땐 한가지 케이스가 타임아웃나는데 while문으로 바꾸었더니 되었다고 한다;

# 파이썬은 배열이 없고 list라서 잘라넣는것도 속도에 영향을 줄 것 같아서
#####################풀이#########################
# scores를 오름차순 정렬 후 (alice도 오름차순이므로) 순서대로 비교하되
# 비교한 위치의 값을 저장(nStart)하여 alice의 다음점수 검색시간을 줄일 수 있게 하였다

# 처음으로 처리 속도에 관해 고민해봤던 시간 재밌었다
# 그러고 보니 이스트소프트 코딩테스트때도 몇ms내로 동작하게 하시오 라는 조건이 있었다


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):

    scores = list(set(scores));
    scores.sort()
    
    rank = []
    nStart = 0
    nScoreCnt = len(scores) 
    for i in alice:
        for j in range(nStart, nScoreCnt):
            if i < scores[j] :
                rank.append(nScoreCnt-j+1)
                nStart = j 
                break     
            if j == nScoreCnt-1 :
                rank.append(1)                                     
        
    return rank   

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n') 

    fptr.close()