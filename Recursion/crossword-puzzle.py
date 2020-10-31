# https://www.hackerrank.com/challenges/crossword-puzzle/problem

#코드가 엄청 길어질꺼 같은데 일단 푸는중
#-의 시작점을 찾아서 가로 세로 구분 후 길이를 찾고 길이 후보를 정하고 이어지는곳을 찾고 값넣고 재귀시키고 이런식으로 하려고 했는데 200줄이 넘어갈꺼같고 
# 처리 부분도 너무 많아질꺼같아 새로 푸는 중
# 길이, 가로 세로 구분, 시작점만 가지고 대입해보게
# ------------------------------------------------
# 결국 못푼문제 다른사람의 답을 보니 
# 가로로 세로로 자신이 찾아야 하는 단어 혹은 -가 있는지를 가로 세로 연속적으로
# 길이 만큼 체크하고 후보군을 리스트로 받아서 하나씩 넣어은 뒤 재귀함수를 통해 다음단어를 또 
# 가로 세로로 다 찾아봐서 후보를 넣고 하다가 후보를 넣었을 때 다음 단어의 후보가 자리가 없다면
# 마지막 작업을 원복하고 다른 후보를 삽입 이것을 계속반복..
# 대단하다 진짜... 


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
# def crosswordPuzzle(crossword, words, startpos):
#     nWordCnt = lwords.count  

#     #시작점 찾기
#     if len(startpos) == 0:
#         for i in range(10):
#             nMinusY = crossword[i].find('-')
#             nMinusX = i
#             if nMinusY >= 0:
#                 break
#     else:
#         nMinusX = startpos[0]
#         nMinusY = startpos[1]

#     #가로인지 세로인지 구분
#     if nDown == 2:
#         if nMinusY == 9:
#             nDown = 1
#         elif crossword[nMinusX][nMinusY+1] != '-':
#             nDown = 1
#         else:
#             nDown = 0
    
#     #몇글자 인지 
#     nMinusLen = 0
#     if nDown == 1:
#         for i in range(10-nMinusY):  
#             if crossword[nMinusX+i][nMinusY] == '-':
#                 nMinusLen += 1
#             else:
#                 break
#     else:
#         for i in range(10-nMinusX):
#             if crossword[nMinusX][nMinusY+i] == '-':
#                 nMinusLen += 1
#             else:
#                 break 

#     #다음 이어지는곳 찾기 
#     nNextPos = []
#     if nDown ==1:
#         #포문으로 x값 늘려가며 찾아야함 찾은값으로 다른 후보 값 중 매칭도 되는가 확인
#         for i in range(nMinusLen):
#             if nMinusY == 0:  #우측만 검사
#                 if crossword[nMinusX+i][nMinusY+1] == '-':
#                     nNextPos.append(nMinusX+i)                    
#             elif nMinusY == 9:  #좌측만 검사
#                 if crossword[nMinusX+i][nMinusY-1] == '-':
#                     nNextPos.append(nMinusX+i)                  
#             else:               #양방향 검사
#                 if crossword[nMinusX+i][nMinusY+1] == '-':
#                     nNextPos.append(nMinusX+i)      
#                 elif crossword[nMinusX+i][nMinusY-1] == '-':        
#                     nNextPos.append(nMinusX+i)                                             
#     else:
#         for i in range(nMinusLen):
#             if nMinusX == 0:  #우측만 검사
#                 if crossword[nMinusX+1][nMinusY+i] == '-':
#                     nNextPos.append(nMinusY+i)                    
#             elif nMinusX == 9:  #좌측만 검사
#                 if crossword[nMinusX-1][nMinusY-i] == '-':
#                     nNextPos.append(nMinusY+i)                  
#             else:               #양방향 검사
#                 if crossword[nMinusX+1][nMinusY+i] == '-':
#                     nNextPos.append(nMinusY+i)      
#                 elif crossword[nMinusX-1][nMinusY-i] == '-':        
#                     nNextPos.append(nMinusY+i)     
#     if nNextPos.count == 0:
#         return crossword

#     for i in range(nMinusLen):



# print board
def print_board(board):
	for row in board:
		print(''.join(row))


# get possible locations
def get_poss_locs(board, word):
	poss_locs = []
	length = len(word)
    # horizontal possible location
	for i in range(10):
		for j in range(10 - length + 1):
			good = True
			for k in range(len(word)):
				if board[i][j + k] not in ['-', word[k]]:
					good = False
					break
			if good:
				yield (i, j, 0) # 0 is axis indicator
    # vertical possible location
	for i in range(10 - length + 1):
		for j in range(10):
			good = True
			for k in range(len(word)):
				if board[i + k][j] not in ['-', word[k]]:
					good = False
					break
			if good:
				yield (i, j, 1) # 1 is axis indicator

                
# revert move
def revert(board, word, loc):
	i, j, axis = loc
	if axis == 0: # axis 0 is horizontal
		for k in range(len(word)):
			board[i][j + k] = '-'
	else: # axis 1 is vertical
		for k in range(len(word)):
			board[i + k][j] = '-'

# write the word on board at specified loc
def move(board, word, loc):
	i, j, axis = loc
	if axis == 0:
		for k in range(len(word)):
			board[i][j + k] = word[k]
	else:
		for k in range(len(word)):
			board[i + k][j] = word[k]

            
def crosswordPuzzle(board, words):
	global solved

	if len(words) == 0:
		if not solved:
			print_board(board)
		solved = True
		return

	word = words.pop()
	pos_locs = [loc for loc in get_poss_locs(board, word)]

	for loc in pos_locs:
		move(board, word, loc)
		crosswordPuzzle(board, words)
		revert(board, word, loc)

	words.append(word)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
	fptr = sys.stdout

	crossword = []

	for _ in range(10):
		crossword.append(list(input()))		
		# crossword_item = input()
		# crossword.append(crossword_item)

	words = str(input()).split(";")

	solved = False
	# result = crosswordPuzzle(crossword, words)
	crosswordPuzzle(crossword, words)

	# fptr.write('\n'.join(result))
	# fptr.write('\n')

	fptr.close()
