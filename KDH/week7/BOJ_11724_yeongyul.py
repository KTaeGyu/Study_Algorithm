def DFS(start):  
    now = start
    visited[now] = 1   
    for i in range(N+1):
        if arr[now][i] == 1 and not visited[i] == 1:
            visited[i] = 1
            DFS(i)


N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1
while 0 in visited[1:N+1]:
    for i in range(1,N+1):
        if visited[i] == 0:
            DFS(i)
            cnt += 1
print(cnt)
