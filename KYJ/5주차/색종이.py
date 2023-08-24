# 색종이

'''
[입력]
2
0 0 10 10
2 2 6 6

[출력]
64
36
'''

import sys

def coloring(color, MAP, n):    # color은 색깔 정보 행렬, n은 색깔종류
    a1, a2, width, height = color[0], color[1], color[2], color[3]
    for i in range(a2, a2 + height):
        for j in range(a1, a1 + width):
            MAP[i][j] = n           # 색 칠할때마다 덮어버림

N = int(sys.stdin.readline())
arr = []
MAP = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(N):
    m = list(map(int, sys.stdin.readline().split()))
    arr.append(m)

for i in range(N):
    coloring(arr[i], MAP, i + 1)

cntarr = []
for j in range(N):
    cnt = 0
    for row in MAP:
        for a in row:
            if a == j + 1:
                cnt += 1
    cntarr.append(cnt)

for el in cntarr:
    print(el)



            
