import sys
sys.stdin = open("../test.txt", "r")

a = list(input().rstrip())
b = list(input().rstrip())
dp = [[""] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
