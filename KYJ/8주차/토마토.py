# 백준 7576 토마토
'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 
익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 
토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

[입력]
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

[출력]
8


BFS
옛날 물놀이 문제랑 비슷한듯?

'''

from collections import deque
import sys
input = sys.stdin.readline

# 가로, 세로
M, N = map(int,input().split())

# 농장은 2차원 배열
MAP = [list(map(int,input().split())) for _ in range(N)]

# 상하좌우
dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 처음에 토마토가 있는 위치 찾아보기
que = deque([])
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            que.append((i, j, 0))
            MAP[i][j] = 10  # 방문체크 -> 10으로 만들어주기

# 단계를 담을 arr
levels = []

while que:
    cy, cx, level = que.popleft()
    for dy, dx in dire:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < N and 0 <= nx < M:
            if MAP[ny][nx] == 0:
                que.append((ny, nx, level + 1))
                MAP[ny][nx] = 10
    levels.append(level)

# 맵에 0이 남아있다면 -1, 아니면 출력
for row in MAP:
    if 0 in row:
        print(-1)
        exit()

print(max(levels))
