# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/staircase/problem

# coding=<UTF8>

# C처음 할 때 풀던문제 이중포문 써서 하는게 기억이 잘안나서
# for문 내에 스페이스와 샾 찍는걸 별도로 구현..

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    line = 1; 
    temp = 0; 
    for line in range(1, n+1):        
        space= n-line;          
        sharp=line;
        while space > 0 :
            print(' ', end='');
            space = space-1;
        for temp in range(0, line) :
            print('#', end='')
 
        print('');


if __name__ == '__main__':
    n = int(input())

    staircase(n)