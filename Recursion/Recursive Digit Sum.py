# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

#생각나는데로 풀었더니 6번 타임아웃 7 8 9 런타임에러
#아마 int, str 변환과정에서 런타임에러가 아닐까
#엥 그냥 k값을 n합구한뒤 * k 해주니까 싹다 통과 엄청쉽네..

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the superDigit function below.
def superDigit(n, k):
    # sTotal = ''
    # for i in range(k):
    #     sTotal += n    
    # nSum = 0
    # for i in range(len(sTotal)):
    #     nSum = nSum + int(sTotal[i])
    # if len(str(nSum)) == 1:
    #     return nSum
    # else:
    #     nSum = superDigit(str(nSum), 1) 
    # return nSum

    nSum = 0

    for i in range(len(n)):
        nSum = nSum + int(n[i])   

    if k != 1:
        nSum *= k         

    if len(str(nSum)) == 1:
        return nSum
    else:
        nSum = superDigit(str(nSum), 1) 
    return nSum 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
