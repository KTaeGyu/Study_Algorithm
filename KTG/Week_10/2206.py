"""
2206: 벽 부수고 이동하기
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")
from collections import deque


# 시도 2: bfs
def bfs(y, x, ey, ex):
    q = deque()
    q.append((y, x, 1, False))
    v = set()
    v.add((y, x, False))

    while q:
        cy, cx, level, flag = q.popleft()
        if (cy, cx) == (ey, ex):
            return level
        for dy, dx in direction:
            ny, nx = cy + dy, cx + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if (ny, nx, flag) in v:
                continue
            if arr[ny][nx]:
                if flag:
                    continue
                else:
                    v.add((ny, nx, True))
                    q.append((ny, nx, level+1, True))
            else:
                v.add((ny, nx, flag))
                q.append((ny, nx, level+1, flag))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(bfs(0, 0, N-1, M-1))

""" 시도 1 : dfs
sys.setrecursionlimit(1000001)


def dfs(y, x, ey, ex, level, flag):
    if visited[y][x] < level:
        return
    if (y, x) == (ey, ex):
        return
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if visited[ny][nx] <= level+1:
            continue
        if arr[ny][nx]:
            if flag:
                continue
            if not flag:
                flag = True
        visited[ny][nx] = level+1
        dfs(ny, nx, ey, ex, level+1, flag)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[1e9] * M for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Flag = False
dfs(0, 0, N-1, M-1, 1, Flag)
print(visited[N-1][M-1] if visited[N-1][M-1] != 1e9 else -1)
"""
"""
6 4
0100
1110
1000
0000
0111
0000

15
"""