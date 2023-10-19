# SWEA 스노우맨

'''
5 8
1 1 1 1 0 0 0 0
0 0 0 3 0 1 1 1
1 1 1 0 0 1 0 0 
0 0 0 0 0 0 1 0 
2 1 1 1 1 1 1 1

5 8
0 0 0 1 1 1 0 0
1 3 1 1 0 1 1 1
0 0 0 0 0 1 1 0 
0 0 0 0 0 0 1 0 
2 1 1 1 1 1 1 1 


다익스트라로 풀어볼까.....
각각의 칸까지 가는데에 드는 최단높이?

이게 왜
'''
import heapq

N, M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            snowmany = i
            snowmanx = j
        if MAP[i][j] == 3:
            diay = i
            diax = j

# 우선 초기 설정
limits = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    height = abs(i - snowmany) + 1
    limits[i] = [height for _ in range(M)]

# 상하, 좌우
dir1 = [(1, 0), (-1, 0)]
dir2= [(0, 1), (0, -1)]

# visited
visited = []
pq = []
heapq.heappush(pq, (1, 0, snowmany, snowmanx))
limits[snowmany][snowmanx] = 1
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[snowmany][snowmanx] = 1

while pq:
    # h = 현재의 점프 높이
    # limit = 여기까지 올때 드는 최소 높이 = 앞에꺼에 + 1
    nowmax, h, cy, cx = heapq.heappop(pq)
    if nowmax > limits[cy][cx]:
        continue
    
    # 상하로 갈 때,
    for dy, dx in dir1:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < N:
            # 땅이라면, 초기화해줌
            if MAP[ny][nx] != 0 and limits[ny][nx] > nowmax:
                nowmax = max(h, nowmax)
                # limit바꿔주기
                limits[ny][nx] = min(limits[cy][cx], nowmax)
                heapq.heappush(pq, (nowmax, 1, ny, nx))  # 높이 초기화
            # 땅이 아니라면,
            elif MAP[ny][nx] == 0:
                if limits[ny][nx] > nowmax:
                    nowmax = max(h + 1, nowmax)
                    limits[ny][nx] = min(limits[ny][nx], nowmax)
                    heapq.heappush(pq,(nowmax, h + 1, ny, nx))

    # 좌우로 갈 때는 땅이 있어야 갈 수 있음
    if MAP[cy][cx] != 0:
        for dy, dx in dir2:
            ny, nx = cy + dy, cx + dx
            if 0 <= nx < M:
                if MAP[ny][nx] != 0 and visited[ny][nx] == 0:
                    limits[ny][nx] = min(nowmax, limits[cy][cx])
                    visited[ny][nx] = 1
                    heapq.heappush(pq, (nowmax, h, ny, nx))

print(limits[diay][diax])











