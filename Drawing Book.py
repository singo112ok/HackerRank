# https://www.hackerrank.com/challenges/drawing-book/problem

# 펼쳐져 있는 책의 상태를 하나의 인덱스로 보고 
# 최대 인덱스를 구한 후 앞에서 부터 책장을 넘겨야 할 값(인덱스)과
# 뒤에서 넘겨야 할 값을 비교 머리좀 쓴거같다

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    # if p == 0 or p ==1:
    #     return 0
    
    nMaxIndex = int(n/2)
    nForward = int(p/2)
    nBack = nMaxIndex-nForward

    # print(nForward)
    # print(nBack)    

    if nForward >= nBack:
        return nBack
    else:
        return nForward   


    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()