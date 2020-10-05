# https://www.hackerrank.com/challenges/torque-and-development/problem

#처음엔 2차원 배열로 0번도시에 시티 리스트 1번도시에 시티리스트 각각 구한 뒤
#도서관수*(도시수-n) + 길 수*(n) 으로 각각의 시티들의 최소값을 구한뒤 합쳤는데 
#2개의 예제가 답이 틀렸고 10개정도가 타임아웃이 발생했다..

#답만 찾아서 디버깅하며 이해만 한 문제
#우선 도로비용보다 도서관 비용이 저렴하면 모든곳에 도서관을 지으면된다(if c_lib < c_road: return n*c_lib)
# 그리고 각 도시의 수만큼 2차원 리스트를 만들고 재귀함수로 깊이우선탐색을 하여 이어질수 있는 최대 도로 길이를 구한다(도로가 더 저렴하니 최대 도로길이가 중요)
# 이후 도로길이*도로비용 + (도시의 수 - 도로길이)*도시비용 을 계산한다
# 몇개의 도시가 있는지는 중요하지 않고 최대 몇개의 도로를 이을 수 있는지가 중요했다..
 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from functools import reduce


# Complete the roadsAndLibraries function below.
# def roadsAndLibraries(n, c_lib, c_road, cities):
#     if len(cities) == 0:
#         return n*c_lib
#     elif c_lib < c_road:
#         return n*c_lib

    
#     cities.sort(key=lambda x:x[0])

#     ListCity = []
#     ListCity.append([])    

#     ListCity[0].append(cities[0][0])
#     ListCity[0].append(cities[0][1])                  
    
#     for i in range(1, len(cities)):
        
#         nStart = cities[i][0]
#         nEnd = cities[i][1]
#         for j in range(0, len(ListCity)):
#             if (nStart in ListCity[j]) and (nEnd in ListCity[j]):
#                 break
#             elif (nStart in ListCity[j]) and not(nEnd in ListCity[j]):
#                 ListCity[j].append(nEnd)
#                 break
#             elif not(nStart in ListCity[j]) and (nEnd in ListCity[j]):
#                 ListCity[j].append(nStart)                           
#                 break
            
#             if j == len(ListCity)-1:
#                 ListCity.append([])
#                 ListCity[j+1].append(nStart)
#                 ListCity[j+1].append(nEnd)

#     nNowcnt = 0
#     for i in range(0, len(ListCity)):
#         nNowcnt += len(ListCity[i])

#     nDif = n - nNowcnt
#     for i in range(0, nDif):
#         ListCity.append([1])        

#     nMinSum = 0
#     nMinCost = len(cities)*c_road + len(cities)*c_lib

#     for i in range(0, len(ListCity)):
#         nCityCnt = len(ListCity[i])
#         for j in range(0, nCityCnt):
#             if nMinCost > (c_lib * (nCityCnt-j)) + (c_road * j):
#                 nMinCost = (c_lib * (nCityCnt-j)) + (c_road * j)

#         nMinSum += nMinCost   
#         nMinCost = len(cities)*c_road + len(cities)*c_lib             
    
#     return nMinSum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def dfs(s,arr,visited):
    visited[s]=True
    cost=0
    for i in arr[s]:
        if(not visited[i]):
            cost+=1
            cost+=dfs(i,arr,visited)
    return cost
def roadsAndLibraries(n,m, c_lib, c_road, cities):
    if(c_lib<c_road):
        return c_lib*n
    if(m==0):
        return n*c_lib
    arr=[[0] for i in range(n+1)]
    visited=[False for i in range(n+1)]
    for i in range(1,n+1):
        arr[i][0]=i
    for i in range(m):
        arr[cities[i][0]].append(cities[i][1])
        arr[cities[i][1]].append(cities[i][0])
    vis=0
    for i in range(1,n+1):
        if(not visited[i]):
            vis+=dfs(i,arr,visited)
    cost=(((vis)*c_road)+((n-vis)*c_lib))
    return cost

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, m, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
