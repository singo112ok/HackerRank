# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#갑자기 난이도가.. 빨리풀자 빨리..

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    aDist = z-x
    bDist = z-y
    if aDist < 0:
        aDist *= -1

    if bDist < 0:
        bDist *= -1        

    if aDist==bDist:
        return 'Mouse C'
    elif aDist<bDist:
        return 'Cat A'
    else:
        return 'Cat B'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()