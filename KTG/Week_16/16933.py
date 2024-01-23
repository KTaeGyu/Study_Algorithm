import sys
sys.stdin = open('../test.txt', 'r')
from collections import deque

N, M, K = map(int, input().split())
arr = [list(input()) for n in range(N)]

v = [[[] for _ in range(M)] for _ in range(N)]

# y, x, 낮밤, 벽부술 기회, 이동 횟수
q = deque([[0, 0, True, K, 0]])
v[0][0].append([True, K])

result = []
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while q:
    y, x, t, c, m = q.popleft()
    if y == N - 1 and x == M - 1:
        result.append(m)
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 > ny or 0 > nx or ny >= N or nx >= M:
            continue
        if arr[ny][nx] == '1':
            if c > 0:
                if t:
                    if [not t, c - 1] in v[ny][nx]:
                        continue
                    q.append([ny, nx, not t, c - 1, m + 1])
                    v[ny][nx].append([not t, c - 1])
                else:
                    if [not t, c] in v[y][x]:
                        continue
                    q.append([y, x, not t, c, m + 1])
                    v[y][x].append([not t, c])
        else:
            if [not t, c] in v[ny][nx]:
                continue
            q.append([ny, nx, not t, c, m + 1])
            v[ny][nx].append([not t, c])

print(min(result) + 1)
