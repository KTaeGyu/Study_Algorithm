# 9012번 괄호

# from collections import Counter

# n = int(input())

# for i in range(n): 
#     bracket = list(input())
#     nums = dict(Counter(bracket))

#     if nums['('] == nums[')']:
#         print('YES')
#     else:
#         print('NO')

## runtime error ('(((' 이런경우에는 key가 하나뿐이라 에러 뜸)

# n = int(input())

# for i in range(n): 
#     bra = list(input())
#     nums = {}

#     for j in bra:
#         nums.setdefault(j, 0)
#         nums[j] += 1

#     if len(nums.keys()) == 2:
#         if nums['('] == nums[')']:
#             if bra[0] == ')' or bra[-1] == '()':
#                 print('NO')
#             else:
#                 print('YES')
#         else:
#             print('NO')
#     else:
#         print('NO')

## 얘도 아닌거같음 ('())(()': 이런거 때문에)

## 스택

n = int(input()) # 몇갠지 받고

for j in range(n):
    stack = [] # 비어있는 스택 
    par = list(input()) # 인풋 리스트로 받아서

    for i in par: # 리스트에 있는 값들 하나씩 넣어가면서 스택에 저장
        if i == '(': # 무조건 (으로 시작해야함
            stack.append(1) # ( 나오면 1저장
        else: # )가 나오면 1을 없앤다
            if len(stack) == 0 or stack.count(4) != 0:  # 근데 비어있을 때 ) 나오면 오류가 나므로 보정해줌
                stack.append(4) # 비어있을 때 )가 나오면 4를 저장해줘서 이미 틀렸다는걸 알려줌, 안그러면 오류남...
            else:
                stack.remove(1)
    if len(stack) == 0: # 마지막에 스택이 다시 비게되면 맞다
        print('YES')
    else:
        print('NO')

# 마자땅
