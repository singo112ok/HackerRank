# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen

# 문제 이해가 좀 헷갈렸지만 예제보고 눈치것 알게됬다
# a부터 z까지 배열(alpha)를 만들어 놓고 word값이 몇번째 위치 인지 찾아서 h와 비교 
# 맥스값 찾은뒤 길이 곱

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
    ,'r','s','t','u','v','w','x','y','z']
    nMax = 0
    for i in word:
        nIndex = alpha.index(i)
        if nMax < h[nIndex]:
            nMax = h[nIndex]

    return nMax*len(word)
    



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()