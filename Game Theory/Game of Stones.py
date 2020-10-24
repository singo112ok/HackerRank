# https://www.hackerrank.com/challenges/game-of-stones-1/problem

#!/bin/python3

#답을 쭈욱 뽑아보니 1에서 10까지 수 중 1, 7과 8을 제외하고 모두 first가 이긴다
#7로 나눈 나머지가 0이거나 1이면 Second아니면 first승

import math
import os
import random
import re
import sys

# Complete the gameOfStones function below.
def gameOfStones(n):
    nMod = n % 7
    if (nMod == 0 or nMod ==1):
        return 'Second'
    else:
        return 'First'      



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
