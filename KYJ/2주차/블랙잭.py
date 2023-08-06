# 2798번 블랙잭

N, M = map(int, input().split())        # N이 카드 개수, M이 목표합
nums = list(map(int,input().split()))       # 카드들의 수

max_sum = 0
for i in range(N):              # 그냥 for문 중첩
    for j in range(N):
        if i != j:
            for k in range(N):
                if i != k and j != k:
                    sum_of_sub = nums[i] + nums[j] + nums[k]
                    if sum_of_sub > max_sum and sum_of_sub <= M:
                        max_sum = sum_of_sub

print(max_sum)


# 이건 되네



# def Black_Jack(arr, n, M):
#     max_sum = []          # 부분집합을 다 만들고
#     for i in range(1 << n):
#         sub = []
#         for j in range(n):
#             if i & (1 << j):
#                 sub.append(arr[j])
#         if len(sub) == 3:
#             max_sum.append(sum(sub)) 
#     maxval = max_sum[0]       # 부분집합에서 최대값 구해줬다
#     for i in max_sum:
#         if i >= maxval and i <= M:
#             maxval = i
#     return maxval
    
# print(Black_Jack(nums, N, M))

# # # 시간 초과남



