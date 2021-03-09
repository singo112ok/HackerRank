# https://www.hackerrank.com/challenges/kangaroo/problem

# 빠르게 리턴주는값 먼저 지정해놓고 두번째 캥거루가 지나칠때까지 반복

# #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'

    locate1 = x1
    locate2 = x2

    while (locate1 <= locate2):
        if locate1 == locate2:
            return 'YES'           
        locate1 = locate1 + v1
        locate2 = locate2 + v2         
    return 'NO'



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    # print(result)

    fptr.write(result + '\n')

    fptr.close()