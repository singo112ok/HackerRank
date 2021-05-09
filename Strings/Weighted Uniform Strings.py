# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

# 난이도 : easy, 통과율 : 73.23%

# 문제: a~z까지 각 문자에는 매칭되는 가중치 값이 있다, 문자는 오름차순 정렬되어있다,
# 동일한 문자의 경우 본 문자의 가중치값, 문자 누적의 가중치 값을 모두 가진다
# 두번째 파라메타로 넘어온 값들이 해당 문자열의 가중치에 존재하면 각각 YES, NO로 리턴하라

#!/bin/python3

import math
import os
import random
import re
import sys



def weightedUniformStrings(s, queries):    
    weight : set = set()
    before_char : str = ''
    weightsum : int = 0
    result : list = []
    weight_chart : dict = {}

    # 가중치 표 세팅
    for i in range(0, 26):
        weight_chart[chr(97+i)] = i+1

    # 연속된 문자인경우 누적합, 아닐경우 가중치 표에 맞는 값을 set에 추가
    for i in s:
        if i == before_char:
            weightsum += weight_chart[i]
            weight.add(weightsum)
        else:
            weightsum = weight_chart[i]
            before_char = i
            weight.add(weight_chart[i])

    #두번째 파라메타로 넘어온 값이 set내에 있는지 확인하여 리스트 구성, 리턴
    for i in queries:
        if(i in weight):
            result.append('Yes')              
        else:
            result.append('No') 
    
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
