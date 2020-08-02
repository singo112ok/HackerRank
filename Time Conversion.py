# https://www.hackerrank.com/challenges/time-conversion/problem

# 고생했던문제, 변수형을 선언해주지 않아도 되는 파이썬 특징 때문에 오히려 고생함
# str과 int로 자꾸 바꾸다가 조건문에서 빠져나감 변수는 현재의 형에 대해서 어느정도 파악해두고
# 어딘가 값을 대입할때만 형을 바꾸는게 좋을 것 같다

#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    minsec = s[3:8]
    h = s[0:2]
    if s.find('PM')>0 :
        if int(h) < 12 :
            h = int(h)+12  
    elif h == '12':
        h = '00' 
    return str(h)+ ':' + minsec

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    f = sys.stdout

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
