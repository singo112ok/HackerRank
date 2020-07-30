# https://www.hackerrank.com/challenges/simple-array-sum/problem

# 파이썬을 차근차근 맛보며 적응하기에 좋은난이도 ^^;
# 이 때 당시엔 list를 for문에서 더 편하게 쓸 수 있었는데 몰라서 range를 
# 구했었다.. 지금 수정한다면 
# for i in ar:
#     sum = sum + i


import os
import sys

#
# Complete the simpleArraySum function below.
#


def simpleArraySum(ar):
    sum = 0;
    for i in range(0,ar_count):
        sum = sum + ar[i]
    return sum   

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr = sys.stdout    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()