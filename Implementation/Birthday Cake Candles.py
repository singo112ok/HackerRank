#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#math 라이브러리로 간단하게 근데 이래도 되는건가..?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxval = max(ar)
    maxcount = 0
    for i in range(0, len(ar)):
        if(ar[i] == maxval):
            maxcount =  maxcount + 1              

    return maxcount




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()