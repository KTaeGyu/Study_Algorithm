import sys
sys.setrecursionlimit(10**4)
N, M ,R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []
cnt = 0

def DFS(start):
    global cnt
    now = start
    cnt += 1
    visited[now] = cnt
    for i in arr[now]:
        if i in arr[now] and not visited[i]:
            visited[i] = 1
            DFS(i)



for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


for i in range(N):
    arr[i].sort()

DFS(R)

print(*visited[1:],sep='\n')

