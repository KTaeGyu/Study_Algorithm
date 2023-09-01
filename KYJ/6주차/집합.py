# 11723번 집합

'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

[입력]
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

[출력]
check 연산이 주어질때마다, 결과를 출력한다.
'''
# 비트 마스킹 이용


import sys 

M = int(sys.stdin.readline())
S = 0
for _ in range(M):
    quest = sys.stdin.readline().rstrip().split()
    if quest[0] == 'all':
        S = (1 << 20) - 1
    elif quest[0] == 'empty':
        S = 0
    else:
        q, num = quest[0], quest[1]
        num = int(num) - 1
        if q == 'add':
            S = S | (1 << num)
        elif q == 'remove':
            S = S & ~(1 << num)
        elif q == 'check':
            if S & (1 << num):
                print(1)
            else:
                print(0)
        elif q == 'toggle':
            S = S ^ (1 << num)

# 시간이 너무 빡빡해


# S = 0
# num = 5
# S |= set(1 << num)
# print(S)













# # 시간 초과남

# def ziphab(quest):
#     global S
#     if quest == 'all':
#         S = {i for i in range(1, 21)}
#         return S
#     elif quest == 'empty':
#         S.clear()
#         return S
#     else:
#         q, num = quest.split()
#         num = int(num)
#         if q == 'add':
#             S.add(num)
#         elif q == 'remove':
#             S.discard(num)
#         elif q == 'check':
#             if num in S:
#                 print(1)
#             else:
#                 print(0)
#         elif q == 'toggle':
#             if num in S:
#                 S.remove(num)
#             else:
#                 S.add(num)


# M = int(input())
# S = set()
# for _ in range(M):
#     ziphab(input())
   
