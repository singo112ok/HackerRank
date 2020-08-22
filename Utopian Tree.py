# https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

# 엄청 쉬운문제
# 다만 값을 리스트로 쭉 받아와서 답을 리스트로 주는게 아니고
# 값을 하나씩 받으며 함수를 계속 반복하는거로 봐서
# 공식을 만들어 내는건 줄 알았다 또 타임아웃일줄..
# n = (n/2) + @ 이런식으로 만들다가 도저히 안나와서 그냥 하니 됬다
# 답을보니 제곱으로 공식을 만들 수 있었다..
# (2,(n+1)/2+1)-1-(n%2)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    nResult = 1
    for i in range(0,n):      
        if i%2 == 0:
            nResult *= 2
        else:
            nResult += 1  
    return nResult


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()


import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    nResult = 1
    for i in range(0,n):      
        if i%2 == 0:
            nResult *= 2
        else:
            nResult += 1  
    return nResult


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()