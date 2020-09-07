# https://www.hackerrank.com/challenges/big-sorting/problem

# 이미 sort가 NlogN시간 복잡도라는데 여기서 뭘 더 빠르게 할 수 있을지..
# 그나마 문자열이니 문자의 길이로 먼저 순위를 나누고 동일 길이만 별도로 sort돌려볼까 했는데
# 큰 차이가 없을것같음 오히려 느릴꺼같은 확신이 들어 포기

#!/bin/python3

import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    unsorted.sort(key=int)     
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
