# https://www.hackerrank.com/challenges/bon-appetit/problem

#문제 내용이 재밌었다... 이해도 쉽게 갔고
#알고리즘은 간단

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    del bill[k]
    realpay = int(sum(bill) / 2)

    if realpay == b:
        result = "Bon Appetit"
    else:
        result = b - realpay

    print(result)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)


