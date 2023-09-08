# 18870번 좌표 압축
'''
n개의 좌표를 압축할때, 각각의 자리는 원래 숫자보다 작은애가 몇개인지 숫자로 나타내기


[입력]
5
2 4 -10 4 -9



[출력]
2 3 0 3 1

'''


# 딕셔너리 이용

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
setarr = set(arr)
sarr = sorted(setarr)
numdic = {}     # 숫자 : 인덱스
for i in range(len(sarr)):
    numdic[sarr[i]] = i

for num in arr:
    print(numdic[num], end= ' ')









# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))
# setarr = set(arr)
# sarr = sorted(setarr)
# result = []

# for num in arr:
#     a = sarr.index(num)     # index가 시간복잡도가 좀 높음 -> 딕셔너리로
#     print(a,end=' ')

