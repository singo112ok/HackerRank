# https://www.hackerrank.com/challenges/apple-and-orange/problem

# 점점 본문이 길어져서 부담스러우나 문제 자체는 쉽다
# 집을 넘어가는 케이스를 생각안해서 좀더 걸렸다

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    arrA = []
    arrO = []
    cntA = 0;
    cntO = 0;

    for i in apples:
        if ((a+i >= s) and (a+i <= t)):
            cntA = cntA + 1           
        # arrA.append(a+i)
    for i in oranges:
        if ((b+i <= t) and (b+i >= s)):
            cntO = cntO + 1        
        # arrO.append(b+i)
    print(cntA)
    print(cntO)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)