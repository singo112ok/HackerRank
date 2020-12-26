# https://www.hackerrank.com/challenges/zig-zag-sequence/problem

# 지그재그 시퀀스 중간 배열 위치 이전은 오름차순 이후는 내림차순 중간은 최대값
# 예제가 잘못되어있어서 헷갈렸다
# 최초 정렬 후 가장큰값(가장 마지막에 있는값)과 가운데 값 변경 후
# 뒤에서부터 내림차순 정렬


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1              #수정1 : 배열은 0번부터 시작함
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2                          #수정2 : 위와 동일한 이유
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1                     #수정3 : 끝에서 앞으로 오는것이기에 +가 아닌 -

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)






