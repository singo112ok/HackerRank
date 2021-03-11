# https://www.hackerrank.com/challenges/extra-long-factorials/problem

# Medium  Rate: 95.53%

#미디엄이래서 풀었는데 속았다.. 펙토리얼 만드는문제




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n >= 1:
        return n * extraLongFactorials(n-1)
    else:
        return 1
    

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
