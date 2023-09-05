import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


"""
def dfs(cy, cx, ey, ex, h):
    if (cy, cx) == (ey, ex):
        global cnt
        cnt += 1
        return
    for i in range(3):
        ny, nx = cy + direction[(i + h) % 4][0], cx + direction[(i + h) % 4][1]
        if 0 <= ny < N and 0 <= nx < N and not arr[ny][nx] and (ny, nx) not in v:
            nh = (h + i - 1) % 4
            v.add((ny, nx))
            if i + h == 2:
                if arr[ny-1][nx] != 1 and arr[ny][nx-1] != 1:
                    dfs(ny, nx, ey, ex, nh)
            else:
                dfs(ny, nx, ey, ex, nh)
            v.remove((ny, nx))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
v = set()
head = [0, 1, 2]
direction = [(N, N), (0, 1), (1, 1), (1, 0)]

if arr[0][0] != 1 and arr[0][1] != 1:
    dfs(0, 1, N-1, N-1, 0)

print(cnt)
"""