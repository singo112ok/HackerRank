# https://www.hackerrank.com/challenges/plus-minus/problem

# print문 익혀보는시간...

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    i = 0.;
    po = 0.;
    ne = 0.;
    ze = 0.;

    for i in range(0, n):
        if arr[i] > 0:
            po = po+1
        elif arr[i] < 0:
            ne = ne+1
        else :
            ze = ze+1
    
    print('{00:.6f}'.format(po/(po+ne+ze)));
    print('{00:.6f}'.format(ne/(po+ne+ze)));
    print('{00:.6f}'.format(ze/(po+ne+ze)));    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)