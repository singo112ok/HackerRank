# https://www.hackerrank.com/challenges/electronics-shop/problem

# 엄청 쉬운문제 값이 정렬되어있다면 전체 탐색이 아닌 뒤에서 부터 구해볼까 싶었는데
# 그냥 전체탐색 번역없이 풀기 잘하는중!

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):   
    nMax = 0
    for i in keyboards:
        for j in drives:
            nSum = i+j
            if nSum <= b:
                if nSum > nMax:
                    nMax = nSum

    if nMax == 0:
        nMax = -1

    return nMax


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
