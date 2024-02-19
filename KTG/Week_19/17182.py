import sys
sys.stdin = open('../test.txt', 'r')
from collections import deque

N, K = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

for i in range(N):
    for j in range(N):
        for k in range(N):
            g[j][k] = min(g[j][k], g[i][k] + g[j][i])
ans = float('inf')


def dfs(start, cost, cnt):
    global ans
    if cnt == N:
        ans = min(ans, cost)
        return
    for x in range(N):
        if visited[x]:
            continue
        visited[x] = 1
        dfs(x, cost + g[start][x], cnt + 1)
        visited[x] = 0


visited = [0] * N
visited[K] = 1
dfs(K, 0, 1)

print(ans, g)
