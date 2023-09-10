"""
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
    1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
    i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp0 = [0] * N
dp1 = [0] * N
dp2 = [0] * N
for i in range(N):
    if i == 0:
        dp0[i] = arr[i][0]
        dp1[i] = arr[i][1]
        dp2[i] = arr[i][2]
    else:
        dp0[i] = min(dp1[i-1] + arr[i][0], dp2[i-1] + arr[i][0])
        dp1[i] = min(dp2[i-1] + arr[i][1], dp0[i-1] + arr[i][1])
        dp2[i] = min(dp0[i-1] + arr[i][2], dp1[i-1] + arr[i][2])
print(min(dp0[N-1], dp1[N-1], dp2[N-1]))



""" 1트 순열 완탐: 시간초과
bit = [-1] * N
result = float('inf')


def solve(i, n):
    if i == n:
        global result
        add = 0
        for i in range(n):
            add += arr[i][bit[i]]
        if result > add:
            result = add
        return
    else:
        if bit[i-1] != 2:
            bit[i] = 2
            solve(i + 1, n)
        if bit[i-1] != 1:
            bit[i] = 1
            solve(i + 1, n)
        if bit[i-1] != 0:
            bit[i] = 0
            solve(i + 1, n)


solve(0, N)
print(result)
"""
"""
3
26 40 83
49 60 57
13 89 99

96
"""