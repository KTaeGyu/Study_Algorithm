import sys
sys.stdin = open("../test.txt", "r")

N, M, H = map(int, input().split())

# 초기 상태: 높이가 0인 경우 1, 나머지 0
dp = [[1] + [0] * H for i in range(N + 1)]

# 각 학생별
for i in range(1, N + 1):
    # 이전 블럭들의 설치 가능한 경우를 가져옴
    dp[i] = dp[i - 1].copy()
    # 이번 학생의 블럭을 입력
    blocks = list(map(int, input().split()))
    # 각 블럭별
    for block in blocks:
        # 이전 경우에서 높이를 초과하지 않도록 가능한 경우들을 더함
        for j in range(block, H + 1):
            dp[i][j] += dp[i - 1][j - block]

print(dp[N][H] % 10007)
