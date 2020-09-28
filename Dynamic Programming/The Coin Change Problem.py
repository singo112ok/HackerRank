# https://www.hackerrank.com/challenges/coin-change/problem

# 처음엔 재귀함수로 동전이 큰 순서대로 최대로 사용할 수 있는개수를 구하고 부족한 
# 동전을 하위 동전에서 구하는식으로 반복하여 금액이 딱맞을경우 카운트를 추가하는식으로 하였으나
# 일부만 통과하고 대부분에서 타임아웃이 발생하고 몇개케이스에서 에러도 발생
# 이후 들으니 이런식으로 푸는공식이 있다고 한다
# [1]+[0]*n 을 구성해놓고
# 코인 1번으로 0 1 2 3 4 .... 값을 만들 수 있는 개수를 배열에 누적시키고
# 코인 2번으로 값을 만들 수 있는개수를 누적시키고 하는방식으로 하는데 
# 그 공식이 아래 이중포문과 동일

#!/bin/python3

import math
import os
import random
import re
import sys

# def FindMod(n, c, index):    
#     AnsCnt = 0        

#     if index == len(c):
#         return 0
#     elif n<c[index] :
#         return FindMod(n, c, index+1)


#     divVal = int(n/c[index])
#     if divVal == 0:
#         return FindMod(n, c, index+1)


#     for i in range(0, divVal+1):
#         if index != 0 and i == divVal:            
#             AnsCnt = FindMod(modVal,c, index+1)     
#             break       
#         modVal = n - c[index]*(divVal+1-i)

#         if modVal > 0:
#             AnsCnt = FindMod(modVal,c, index+1)  
#         else:
#             AnsCnt += 1            
#             continue  

#     return AnsCnt


# def getWays(n, c):
    
#     TotalAns = 0
#     c = sorted(c, reverse=True)
#     TotalAns = TotalAns + FindMod(n, c, 0)

#     return TotalAns     
    
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
