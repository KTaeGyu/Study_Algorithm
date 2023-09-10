"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109
"""
import sys
sys.stdin = open("../test.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
idx_arr = []
for i in range(N):
    idx_arr.append([arr[i], i])
idx_arr.sort(key=lambda x: x[0])
dp = [0]*N
dp[0] = idx_arr[0] + [0]
for i in range(1, N):
    if idx_arr[i][0] == idx_arr[i-1][0]:
        dp[i] = idx_arr[i] + [dp[i-1][2]]
    else:
        dp[i] = idx_arr[i] + [dp[i-1][2] + 1]
dp.sort(key=lambda x: x[1])
for i in range(N):
    print(dp[i][2], end=' ')




"""
5
2 4 -10 4 -9

2 3 0 3 1
"""