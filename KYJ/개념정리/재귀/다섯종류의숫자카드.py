# 다섯 종류의 숫자 카드

# 카드 종류가 다섯개 있을 때, 거기서 중복으로 카드를 뽑는다. 
# 인접한 순서의 카드와 차이가 3이하로 차이나는 순열이 몇가지 인지를 구하기
# 재귀호출을 이용하여 구하기

#### 
card = list(input())
path = [0] * 4 # 카드를 4장 뽑는다 -> 경로가 4
cnt = 0

def card_cnt(level):  # level은 현재 뽑은 카드의 수
    global cnt
    # 4장의 카드를 뽑으면 경우의수 증가
    if level == 4:
        cnt += 1
        return 
    
    for i in range(5):
        path[level] = card[i] # 현재 레벨 경로에 선택한 카드 저장
        # 카드 간의 차이가 4 이상이면 다음 카드를 선택(백트래킹)
        if int(path[level]) - int(path[level - 1]) >= 4:
            continue
        if int(path[level - 1]) - int(path[level]) >= 4:
            continue
        # 다음 레벨로 재귀 호출
        card_cnt(level + 1)

card_cnt(0)
print(cnt)












# nums = list(map(int,list(input())))
# nums_list = [[], [], [], [], []]
# def fun(n):
#     for i in nums:
#         if i - n > 3 or n - i > 0:
#             continue
#         else:
#             nums_list[n-1].append(i)


# fun(1)
# print(nums_list)




# numlist = [[], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [2, 3, 4, 5]]


# def fun(n):
#     global cnt
#     ans = 0
#     cnt += 1
#     if cnt < 5:
#         for i in numlist[n]:
#             ans += fun(i)
#         return ans
#     else:
#         return len(numlist[n])
    
# result = 0

# for k in nums:
#     cnt = 0
#     result += fun(k)

# print(result)


