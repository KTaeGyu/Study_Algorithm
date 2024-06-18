import sys
sys.stdin = open('./12865.txt', 'r')

N, K = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    W, V = map(int, input().split())
    for k in range(1, K + 1):
        if W > k:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - W] + V)

print(dp[N][K])

