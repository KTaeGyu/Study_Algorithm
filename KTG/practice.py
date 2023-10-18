import sys
sys.stdin = open("test.txt", "r")
from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x, arr[0][0]))
    v = [[float('inf')] * N for _ in range(N)]
    v[0][0] = arr[0][0]
    while q:
        cy, cx, fuel = q.pop()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if 0 > ny or ny >= N or 0 > nx or nx >= N:
                continue
            if v[ny][nx] <= fuel + arr[ny][nx]:
                continue
            q.append((ny, nx, fuel + arr[ny][nx]))
            v[ny][nx] = fuel + arr[ny][nx]
        if (cy, cx) == (TN[0], TN[1]):
            if v[TN[2]][TN[3]] <= fuel + TN[4]:
                continue
            q.append((TN[2], TN[3], fuel + TN[4]))
            v[TN[2]][TN[3]] = fuel + TN[4]
        if (cy, cx) == (TN[2], TN[3]):
            if v[TN[0]][TN[1]] <= fuel + TN[4]:
                continue
            q.append((TN[0], TN[1], fuel + TN[4]))
            v[TN[0]][TN[1]] = fuel + TN[4]
    return v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    TN = list(map(int, input().split()))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ans = bfs(0, 0)[N-1][N-1]
    print(ans)

"""
1
6 1
5 1 8 0 5 4 
7 6 4 5 3 5 
4 0 2 7 8 6 
3 2 8 7 8 3 
9 0 0 0 2 8 
4 9 3 5 4 0 
1 3 1 5 1
"""