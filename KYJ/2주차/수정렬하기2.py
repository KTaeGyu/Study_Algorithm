# 2751번 수 정렬하기 2

# N = int(input())
# nums = []
# for i in range(N):
#     nums.append(int(input()))
# nums.sort()
# for num in nums:
#     print(num)


# # python으로 하면 시간 초과, pypy로 하면 성공
# 그냥 pypy 사용함




# # 카운트정렬을 한번 써보자

# N = int(input())
# nums = []
# for i in range(N):
#     nums.append(int(input()))

# count = [0] * (max(nums) + 1)
# for num in nums:
#     count[num] += 1

# for i in range(1,len(count)):
#     count[i] += count[i - 1]

# new_nums = [0] * len(nums)

# for j in reversed(range(len(nums))):
#     new_nums[count[nums[j]]-1] = nums[j]
#     count[nums[j]] -= 1

# for i in new_nums:
#     print(i)
# 이것두 시간초과

import sys # 시간 최대한 줄이기 위해 input도 바꿔준다

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
print(*nums, sep = '\n')

# 이렇게 하니까 파이썬으로도 가능