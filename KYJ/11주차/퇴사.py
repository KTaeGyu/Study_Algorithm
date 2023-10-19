# 백준 14501번 퇴사

'''
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 
남은 N일 동안 최대한 많은 상담을 하려고 한다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 
상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
'''
# Bottom up
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i+ lst[i][0], N + 1): # 상담이 끝나는 날부터 끝까지
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]
print(dp[-1])



# Top down
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    # i 일에 상담이 하는게 퇴사일이 넘는다면 ㄴㄴ
    if i + lst[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        # i일에 상담을 하는거랑 안하는 것 중 큰걸로
        dp[i] = max(dp[i + 1], lst[i][1] + dp[i + lst[i][0]])

print(dp[0])


'''
DP시러............................
'''