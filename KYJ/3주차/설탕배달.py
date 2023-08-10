# # 2839번 설탕배달

'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다.

봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 
봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

'''


# GPT님 풀이

## Dynamic Programming 방법을 이용해서 풀어달라고 했음
def min_bags_for_sugar(N):
    dp = [float('inf')] * (N+1)  # 초기값 설정 , min값을 찾아야하므로 초기값들을 무한대로 설정
    dp[0] = 0
    
    for i in range(3, N+1):
        if dp[i-3] != float('inf'):
            dp[i] = min(dp[i], dp[i-3] + 1)
        if dp[i-5] != float('inf'):
            dp[i] = min(dp[i], dp[i-5] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1

N = int(input())
result = min_bags_for_sugar(N)
print(result)












# 직접 푼 풀이 


# N = int(input())

# cnt = 0
# is_true = True
# # 우선 N을 5로 나눠본다
# a1, a2 = divmod(N, 5) 

# # 만약 몫이 0이면, 즉 N이 5보다 작으면
# if a1 == 0:
#     # 나머지를 3으로 나눠본다
#     if a2 % 3 != 0:
#         is_true = False
#         # 만약 그 나머지가 3으로 나눠떨어지지 않으면 안되므로 땡
#     else:
#         cnt = a2 // 3
#         # 나머지가 3으로 나눠 떨어지면 그게 봉지 개수
# elif a2 % 3 == 0:
#     # 5로 나눴을 때, 나머지가 3으로 나눠 떨어지면
#     cnt = a1 + a2 // 3
# elif a2 % 3 != 0:
#     # 5로 나눴을 때, 나머지가 3으로 나눠 떨어지지 않는다면
#     while a2 % 3 != 0:
#         a1 -= 1
#         a2 += 5
#         if a1 < 0: # 하다가 몫이 -가 되면 실패 = -1 출력
#             is_true = False
#             break
#     cnt = a1 + a2 //3

# if is_true:
#     print(cnt)
# else:
#     print(-1)
    