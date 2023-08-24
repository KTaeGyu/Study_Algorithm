# 2559번 수열
'''
슬라이싱을 하니까 자꾸 시간초과가 뜸
처음 계산해둔 총합에 앞에껀 빼고 뒤에 꺼 더하고 하는 식으로 최대한 시간 줄이기
'''
N, K = map(int,input().split())
nums = list(map(int, input().split()))


numsum = sum(nums[:K])
maxsum = numsum

for i in range(N - K):
    numsum -= nums[i]
    numsum += nums[K + i]
    if numsum >= maxsum:
        maxsum = numsum

print(maxsum)



# N, K = map(int,input().split())
# nums = list(map(int, input().split()))

# p = 0
# maxs = 0

# for i in range(N - K + 1):
#     nums_sum = sum(nums[p + i:p + i + K])        # 슬라이싱은 시간이 오래걸린다.
#     if nums_sum >= maxs:
#         maxs = nums_sum
# print(maxs)