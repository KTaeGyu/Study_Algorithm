# # 1차시도
# N = int(input())
# C_N = N
# sugar = [5, 3]
# cnt = 0
# n_cnt = 0
# for i in sugar:
#     a = C_N // i
#     C_N %= i
#     cnt += a
# if C_N != 0:
#     b = N // 3
#     N %= 3
#     n_cnt += b
#     cnt = n_cnt
#     if N != 0:
#         cnt = -1
# print(cnt)

# # 2차시도
# N = int(input())
# C_N = N
# sugar = [5, 3]
# cnt = 0
# n_cnt = 0
# for i in sugar:
#     a = C_N // i
#     C_N %= i
#     cnt += a
#     n_cnt = 0
# for j in range(1,3):
#     if C_N != 0:
#         C_N += 5*j
#         b = C_N // 3
#         C_N %= 3
#         n_cnt += b
#         cnt = n_cnt
#         if C_N != 0:
#             cnt = -1
# print(cnt)

#3차시도
# N = int(input())
# C_N = N
# cnt = 0
# n_cnt = 0
# sugar = [5, 3]
# while True:
#     n_cnt = 0
#     for i in sugar:
#         a = C_N //i
#         C_N %= i
#         cnt += a

# 정답
def min_sugar_bags(n):
    # 무한대로 초기화된 배열 생성
    dp = [float('inf')] * (n + 1)
    # 0 킬로그램은 0개의 봉지로 만들 수 있음
    dp[0] = 0

    # 각각의 봉지 무게에 대해 최소 봉지 개수 계산
    for weight in [3, 5]:
        for i in range(weight, n + 1):
            dp[i] = min(dp[i], dp[i - weight] + 1)

    # 정확한 무게를 만들 수 없는 경우 -1 반환
    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]


# 입력 받기
n = int(input())
# 최소 봉지 개수 출력
print(min_sugar_bags(n))
