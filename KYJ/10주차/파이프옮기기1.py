# 백준 17070 파이프 옮기기
'''
BFS로는 뭔짓을해도 계속 시간초과가남...
DFS로 바꿔주고 pypy로 했을 때만 시간초과가 안난다...

가로(1), 대각(2), 세로(3)
'''

import sys
input = sys.stdin.readline

dir1 = [(0, 1), (1, 1)] # 가로, 대각
dir2 = [(0, 1), (1, 1), (1, 0)] # 가로, 대각, 세로
dir3 = [(1, 1), (1, 0)] # 대각, 세로

N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]
visitied = [[0 for _ in range(N)] for _ in range(N)]

que = [(0, 1, 1)]    # 좌표, 방향
while que:
    cy, cx, dire = que.pop()
    if cy == N - 1 and dire == 3:
        continue
    elif cx == N - 1 and dire == 1:
        continue
    else:
        if dire == 1:
            for i in range(2):
                ny, nx = cy + dir1[i][0], cx + dir1[i][1]
                if 0 <= ny < N and 0 <= nx < N:
                    if MAP[ny][nx] == 0:    # 비어있어야하고
                        if i == 1:  # 대각선이라면
                            if MAP[ny - 1][nx] == 0 and MAP[ny][nx - 1]== 0:
                                visitied[ny][nx] += 1
                                que.append((ny, nx, 2))
                        else:
                            visitied[ny][nx] += 1
                            que.append((ny, nx, i + 1))
        elif dire == 2:
            for i in range(3):
                ny, nx = cy + dir2[i][0], cx + dir2[i][1]
                if 0 <= ny < N and 0 <= nx < N:
                    if MAP[ny][nx] == 0:
                        if i == 1:  # 대각선이라면
                            if MAP[ny - 1][nx] == 0 and MAP[ny][nx - 1]== 0:
                                visitied[ny][nx] += 1
                                que.append((ny, nx, 2))
                        else:
                            visitied[ny][nx] += 1
                            que.append((ny, nx, i + 1))
        elif dire == 3:
            for i in range(2):
                ny, nx = cy + dir3[i][0], cx + dir3[i][1]
                if 0 <= ny < N and 0 <= nx < N:
                    if MAP[ny][nx] == 0:
                        if i == 0:  # 대각선이라면
                            if MAP[ny - 1][nx] == 0 and MAP[ny][nx - 1]== 0:
                                visitied[ny][nx] += 1
                                que.append((ny, nx, 2))
                        else:
                            visitied[ny][nx] += 1
                            que.append((ny, nx, i + 2))

print(visitied[N - 1][N - 1])