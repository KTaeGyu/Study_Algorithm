# 10816번 숫자카드2
# import sys

# card_num = sys.stdin.readline() # 상근이의 카드 갯수
# card_nums = sys.stdin.readline().split() # 상근이가 가지고 있는 카드들의 리스트
# card_nums = list(map(int,card_nums))
# iden_num = sys.stdin.readline() # 판별해야하는 갯수
# iden_nums = sys.stdin.readline().split() # 판별해야하는 숫자들의 리스트
# iden_nums = list(map(int,iden_nums))

# nums_dict = {}
# for num in iden_nums:
#     nums_dict[num] = 0

# for key in nums_dict.keys():
#     for num in card_nums:
#         if key == num:
#             nums_dict[key] += 1

# for val in nums_dict.values():
#     print(val,end=' ')

## 시간 초과가 납니다//


# count를 씁시다
# card_num = int(input())
# card_nums = list(map(int,input().split()))
# iden_num = int(input())
# iden_nums = list(map(int,input().split()))

# for num in iden_nums:
#     cou = card_nums.count(num)
#     print(cou,end = ' ')
#     for i in range(cou):
#         card_nums.remove(num)

## 그래도 시간초과 뜸



## 이번엔 counter써보기로
from collections import Counter

card_num = int(input())
card_nums = list(map(int,input().split()))
iden_num = int(input())
iden_nums = list(map(int,input().split()))

count_nums = Counter(card_nums)
coun = {}
# for key in iden_nums:
#     if key in count_nums.keys():
#         coun[key] = count_nums[key]
#     else:
#         coun[key] = 0

# for val in coun.values():
#     print(val, end = ' ')

for i in iden_nums:
    if i in count_nums:
        print(count_nums[i],end=' ')
    else:
        print(0, end=' ')