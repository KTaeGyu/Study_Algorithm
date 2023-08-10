#문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

#1차시도
# N = int(input())
#
# n_list = [0, 1, 1] #초기값
#
# def bigyo(N):
#     n_list = [0, 1, 1]
#     for i in range(2, N+1):
#         imsi = []
#         if i % 2 == 0 and i % 3 == 0:
#             imsi.append(n_list[i // 2] + 1)
#             imsi.append(n_list[i // 3] + 1)
#             imsi.append(n_list[i - 1] + 1)
#         elif i % 2 == 0:
#             imsi.append(n_list[i // 2] + 1)
#             imsi.append(n_list[i - 1] + 1)
#         elif i % 3 == 0:
#             imsi.append(n_list[i // 3] + 1)
#             imsi.append(n_list[i - 1] + 1)
#         n_list.append(min(imsi))
#         return n_list[]
# print(bigyo(N))

# 정답

def gyesan(n):
    # 무한대로 초기화된 배열 생성
    dp = [float('inf')] * (n + 1)
    # 1을 만들기 위한 최소 연산 횟수는 0회
    dp[1] = 0

    # 2부터 n까지 최소 연산 횟수 계산
    for i in range(2, n + 1):
        # 1을 뺀 경우
        dp[i] = min(dp[i], dp[i - 1] + 1)
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]


# 입력 받기
n = int(input())
# 최소 연산 횟수 출력
print(gyesan(n))

