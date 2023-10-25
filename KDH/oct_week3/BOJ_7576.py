from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
M,N = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            visited[i][j] = -1
        if arr[i][j] == 1: 
            visited[i][j] = 1
            q.append((i,j))


def Toma():
    while q:
        now = q.popleft()
        for k in range(4):
            ny = now[0]+dy[k]
            nx = now[1]+dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[now[0]][now[1]] + 1   
                    q.append((ny,nx))
        

def ansdef():
    ans = visited[0][0]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return print(-1)             
            if ans < visited[i][j]:
                ans = visited[i][j]
    print(ans-1)


Toma()
ansdef()