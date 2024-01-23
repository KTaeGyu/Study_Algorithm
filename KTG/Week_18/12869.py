import sys
sys.stdin = open('../test.txt', 'r')
from collections import deque


def solve(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        ans = min(cnt, ans)
        return
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0
    dp[x][y][z] = cnt
    for dx, dy, dz in ADs:
        solve(x - dx, y - dy, z - dz, cnt + 1)


N = int(input())
SCVs = [0, 0, 0]
HPs = list(map(int, input().split()))
for i in range(N):
    SCVs[i] = HPs[i]
ADs = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]
cnt = 0

q = deque([])
maxS = max(SCVs)
dp = [[[120] * (maxS + 1) for _ in range(maxS + 1)] for _ in range(maxS + 1)]
ans = 1e9

dp[SCVs[0]][SCVs[1]][SCVs[2]] = 0
solve(SCVs[0], SCVs[1], SCVs[2], 0)
print(ans)
