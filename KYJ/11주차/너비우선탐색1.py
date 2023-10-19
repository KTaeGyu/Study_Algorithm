# 백준 24444 알고리즘 수업 - 너비우선탐색1

from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0 for _ in range(N + 1)]
visited[R] = 1

def BFS(start):
    que = deque([start])
    level = 1
    while que:
        now = que.popleft()
        for next in sorted(arr[now]):
            if visited[next] == 0:
                que.append(next)
                level += 1
                visited[next] = level   # visited는 넣을 때

BFS(R)
print(*visited[1:],sep='\n')