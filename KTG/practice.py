import sys

sys.stdin = open('./test.txt', 'r')

n = int(input())

dp = [0] * 25
dp[4] = 1

for i in range(1, 21):
    if i % 2 == 0:
        dp[i + 4] = dp[i + 1] + dp[i + 2] + dp[i + 3]
    else:
        dp[i + 4] = dp[i] + dp[i + 1] + dp[i + 2] + dp[i + 3]

print(dp[n+4])
