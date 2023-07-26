# 1920번 수 찾기

# n = int(input())
# nums = set(map(int, input().split()))
# m = int(input())
# check_nums = list(map(int, input().split()))

# l_nums = len(nums)

# for i in check_nums:
#     check_set = set()
#     check_set.add(i)
#     len_union = len(nums.union(check_set))
#     if len_union == l_nums:
#         print(1)
#     else:
#         print(0)

## 시간 초과 뜸, union이 시간을 많이 쓴듯


n = int(input())
nums = set(map(int, input().split()))
m = int(input())
check_nums = list(map(int, input().split()))

for check in check_nums:
    if check in nums:
        print(1)
    else:
        print(0)

# 그냥 in으로 하니까 해결