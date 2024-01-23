import sys
sys.stdin = open('../test.txt', 'r')

N, K = map(int, input().split())
checkPoints = [list(map(int, input().split())) for _ in range(N)]

INF = 1e10
dp = [[INF] * N for _ in range(K+1)]

dp[0][0] = 0
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + abs(checkPoints[i-1][0] - checkPoints[1][0]) + abs(checkPoints[i-1][1] - checkPoints[i][1])

for i in range(1, K+1):
    for j in range(N):
        if j <= i:
            dp[i][j] = 0
        else:
            pass
print(checkPoints)
print(dp)