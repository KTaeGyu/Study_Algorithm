import sys
sys.stdin = open("../test.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dp = []
    dp.append(1)
    dp.append(2)
    dp.append(4)
    for i in range(3, n):
        nxt = dp[i-1] + dp[i-2] + dp[i-3]
        dp.append(nxt)
    print(dp[n-1])