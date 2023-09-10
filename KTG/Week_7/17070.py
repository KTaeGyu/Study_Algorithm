import sys
from pprint import pprint
sys.stdin = open("../additional/input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if arr[i][j] == 0:
            if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[N-1][N-1]))
