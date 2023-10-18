'''
A형기출

산악 구조를 위한 로봇이 있습니다. 
이 로봇은 연료 소모를 최대한 적게 하면서 조난자에게 이동하여 구출하려고 합니다. 
산악 구조는 N x N 크기의 지도로 정보가 주어집니다.
각 칸의 값은 땅의 높이를 표현하며,
구조 로봇은 상, 하, 좌, 우 방향으로만 이동이 가능합니다. 
구조 로봇의 연료 소모량은 다음과 같습니다.
내리막길 (현재 위치에서 더 낮은 곳으로 이동할 때)에서는 연료가 소모되지 않습니다. 
오르막길 (현재 위치에서 더 높은 곳으로 이동할 때)에서는 높이 차이의 2배가 소모됩니다.
평지 (현재 위치에서 같은 높이로 이동할 때)에서는 1의 연료가 소모됩니다.

해당 산에는 많은 조난자가 발생하여, M개의 터널을 만들었습니다.
각 터널은 두 위치 A, B를 C의 연료만큼 소모하여 자유롭게 이동할 수 있습니다.
단, 터널을 이용하기 시작하면 반대편 위치까지 도착하기 전에 터널을 벗어날 수 없습니다.
(무조건 A->B, B->A로만 갈 수 있습니다.)

구조 로봇의 출발지는 항상 (1, 1)로 고정되어 있으며, 
조난자의 위치는 (N, N)으로 고정되어 있습니다.
조난자의 위치까지 최소 연료를 소비하는 경로를 찾고, 
소모된 연료 값을 출력하는 프로그램을 작성하시오. 

'''
# 다익스트라
import heapq
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def cal(starty, startx, endy, endx):
    pq = []
    heapq.heappush(pq, (starty, startx, 0))
    f = [[float('INF') for _ in range(N)] for _ in range(N)]
    f[starty][startx] = 0
    while pq:
        cy, cx, fu = heapq.heappop(pq)
        if fu > f[cy][cx]:
            continue
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                now = MAP[cy][cx]
                new = MAP[ny][nx]
                if now > new:
                    nextv = fu
                elif now == new:
                    nextv = fu + 1
                else:
                    nextv = fu + 2 * (new - now)
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    heapq.heappush(pq, (ny,nx,nextv))
        for i in range(len(tunnel)):
            if cy == tunnel[i][0] and cx == tunnel[i][1]:
                ny, nx = tunnel[i][2], tunnel[i][3]
                nextv = fu + tunnel[i][4]
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    heapq.heappush(pq, (ny,nx,nextv))
            if cy == tunnel[i][2] and cx == tunnel[i][3]:
                ny, nx = tunnel[i][0], tunnel[i][1]
                nextv = fu + tunnel[i][4]
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    heapq.heappush(pq, (ny,nx,nextv))
    return f[endy][endx]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    tunnel = []
    for _ in range(M):
        ay, ax, by, bx, c = map(int,input().split())
        tunnel.append([ay - 1, ax - 1, by - 1, bx - 1, c])
    ans = cal(0,0,N-1,N-1)
    print(f'#{tc} {ans}')




'''
# BFS
from collections import deque

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def cal(starty, startx, endy, endx):
    que = deque([(starty, startx, 0)])
    f = [[float('INF') for _ in range(N)] for _ in range(N)]
    f[starty][startx] = 0
    while que:
        cy, cx, fu = que.popleft()
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                now = MAP[cy][cx]
                new = MAP[ny][nx]
                if now > new:
                    nextv = fu
                elif now == new:
                    nextv = fu + 1
                else:
                    nextv = fu + 2 * (new - now)
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    que.append((ny, nx, nextv))
        for i in range(len(tunnel)):
            if cy == tunnel[i][0] and cx == tunnel[i][1]:
                ny, nx = tunnel[i][2], tunnel[i][3]
                nextv = fu + tunnel[i][4]
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    que.append((ny, nx, nextv))
            if cy == tunnel[i][2] and cx == tunnel[i][3]:
                ny, nx = tunnel[i][0], tunnel[i][1]
                nextv = fu + tunnel[i][4]
                if nextv < f[ny][nx]:
                    f[ny][nx] = nextv
                    que.append((ny, nx, nextv))
    return f[endy][endx]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    tunnel = []
    for _ in range(M):
        ay, ax, by, bx, c = map(int,input().split())
        tunnel.append([ay - 1, ax - 1, by - 1, bx - 1, c])
    ans = cal(0,0,N-1,N-1)
    print(f'#{tc} {ans}')
'''
























# 생각해보니까 이렇게하면, 터널 2개 이상을 지날때를 못잡음..
# from collections import deque

# dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# def cal(starty, startx, endy, endx):
#     que = deque([(starty, startx, str(startx)+str(starty)+'/')])
#     f = [[float('INF') for _ in range(N)] for _ in range(N)]
#     f[starty][startx] = 0
#     while que:
#         cy, cx, path = que.popleft()
#         if cy == endy and cx == endx:
#             return f[cy][cx]
#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if str(ny)+str(nx) not in path:
#                     now = MAP[cy][cx]
#                     new = MAP[ny][nx]
#                     if now > new:
#                         f[ny][nx] = min(f[ny][nx], f[cy][cx])
#                     elif now == new:
#                         f[ny][nx] = min(f[ny][nx], f[cy][cx] + 1)
#                     else:
#                         f[ny][nx] = min(f[ny][nx], f[cy][cx] + 2 * (new - now))
#                     que.append((ny, nx, path + str(ny) + str(nx) + '/'))

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     # 터널을 안지나고 그냥 갈때
#     ans = cal(0, 0, N -1, N -1)
#     # 터널을 지날때
#     for _ in range(M):
#         ay, ax, by, bx, c = map(int,input().split())
#         # 터널입구까지
#         a = cal(0,0,ay-1,ax-1)
#         # 터널 출구부터 마지막까지
#         b = cal(by -1, bx-1, N -1, N -1)
#         # 앞에 두개랑 터널 지날때
#         temp = a + b + c
#         ans = min(ans, temp)

#     print(f'#{tc} {ans}')




























# from collections import deque
# import pprint

# dir = [(1, 0), (0, 1),(-1, 0),(0, -1)]

# def robot(sy, sx):
#     que = deque([(sy, sx, 0)])
#     result = []
#     f = [[[float('INF'), 0] for _ in range(N)] for _ in range(N)]
    
#     while que:
#         cy, cx, fuel = que.popleft()
#         # 도착 조건
#         if cy == N - 1 and cx == N - 1:
#             pprint.pprint(f)
#             f[cy][cx][0] = min(f[cy][cx][0], fuel)
#             return f[N - 1][N - 1][0]
#         # 만약 터널이면?
#         for i in range(len(tunnel)):
#             if cy == tunnel[i][0]:
#                 if cx == tunnel[i][1]:
#                     f[tunnel[i][2]][tunnel[i][3]][0] = min(f[tunnel[i][2]][tunnel[i][3]][0], fuel + tunnel[i][4])
#                     que.append((tunnel[i][2], tunnel[i][3], fuel + tunnel[i][4]))
#             if cx == tunnel[i][2]:
#                 if cy == tunnel[i][3]:
#                     f[tunnel[i][0]][tunnel[i][1]][0] = min(f[tunnel[i][0]][tunnel[i][1]][0], fuel + tunnel[i][4])
#                     que.append((tunnel[i][0], tunnel[i][1], fuel + tunnel[i][4]))
#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if f[ny][nx][1] < 4:
#                     f[ny][nx][1] += 1
#                     now = MAP[cy][cx]
#                     nxt = MAP[ny][nx]
#                     if now > nxt:
#                         f[ny][nx][0] = min(f[ny][nx][0], fuel)
#                         que.append((ny, nx, f[ny][nx][0]))
#                     elif now == nxt:
#                         f[ny][nx][0] = min(f[ny][nx][0], fuel + 1)
#                         que.append((ny, nx, f[ny][nx][0]))
#                     else:
#                         a = nxt - now
#                         f[ny][nx][0] = min(f[ny][nx][0], fuel + 2 * a)
#                         que.append((ny, nx, f[ny][nx][0]))

#     return result

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     tunnel = []
#     for _ in range(M):
#         ay, ax, by, bx, c = map(int,input().split())
#         tunnel.append((ay - 1, ax -1, by - 1, bx - 1, c))
#     print(f'#{tc} {robot(0,0)}')