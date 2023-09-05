"""
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
"""

import sys
sys.stdin = open("../test.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = []
for i in range(1, n + 1):
    tem = [0] * i
    dp.append(tem)
dp[0][0] = arr[0][0]
for i in range(2, n + 1):
    for j in range(i):
        if j == 0:
            dp[i - 1][j] = arr[i - 1][j] + dp[i - 2][j]
        elif j == i - 1:
            dp[i - 1][j] = arr[i - 1][j] + dp[i - 2][j - 1]
        else:
            dp[i - 1][j] = max(arr[i - 1][j] + dp[i - 2][j], arr[i - 1][j] + dp[i - 2][j-1])
print(max(dp[n-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

30
"""