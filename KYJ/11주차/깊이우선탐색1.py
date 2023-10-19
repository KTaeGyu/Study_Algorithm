# 백준 24479 알고리즘 수업 - 깊이 우선 탐색1
# input이 많으니까 input readline 이용
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# n 점의 갯수 m 간선 갯수 r은 시작점
n, m, r = map(int,input().split()) 
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0 for _ in range(n + 1)]
stack = [r]
level = 1

def dfs(now):
    global level
    # 스택이 비었다면
    if not stack:
        return
    arr[now].sort()
    visited[now] = level
    level += 1
    for next in arr[now]:
        if visited[next] == 0: 
            dfs(next)

dfs(r)
for i in range(1, n + 1):
    print(visited[i])