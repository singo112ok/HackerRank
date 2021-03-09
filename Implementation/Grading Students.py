# https://www.hackerrank.com/challenges/grading/problem

#반올림해서 점수 변경하는문제 간단했다
#여기서부터 list를 for문에 잘 적용해서 쓰고있다

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    roundgrades = []

    for i in grades:
        if i <= 37:
            roundgrades.append(i)            
        elif (i%5) == 3:
            roundgrades.append(i+2)  
        elif (i%5) == 4:
            roundgrades.append(i+1)  
        else : 
            roundgrades.append(i)  

    return roundgrades        
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()