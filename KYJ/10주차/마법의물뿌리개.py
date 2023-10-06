'''
홀수 번째 날에 물을 준 나무는 키가 1만큼 자라고, 
짝수 번째 날에 물을 준 나무는 키가 2만큼 자랍니다. 
물론 어떤 날에는 마법의 물뿌리개를 사용하지 않을 수도 있습니다. 

N개의 나무의 정보가 주어졌을 때, 모든 나무의 키가 
초기의 키가 가장 컸던 나무와 같아지도록 만들기 위한 최소 날짜 수를 계산하시오.

1. 나무의 개수 N은 2 이상 100 이하로 주어집니다. (2 ≤ N ≤ 100) 
2. 주어지는 나무의 초기 높이는 1 이상 120 이하입니다. 

[입력]
3
2
5 5
2
4 2
2
3 4

[출력]
#1 0
#2 2
#3 1

'''
'''
굳이 재귀로 하지말고
그냥 차이를 각각 구하고
그걸로 계산하면 되지않을까
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    namu = list(map(int,input().split()))
    # 목표값
    goal = max(namu)
    # 차이들
    lst = list(map(lambda x: goal - x , namu))
    day = 0
    while sum(lst) > 0:
        day += 1
        # 홀수 날이면
        if day % 2:
            # 만약에 딱 1인애가 있다면
            for i in range(N):
                if lst[i] == 1:
                    lst[i] -= 1
                    break
            # 딱 1인애가 없으면, 홀수인 애부터 바꿔주기
            else:
                for i in range(N):
                    if lst[i] % 2 and lst[i] > 0:
                        lst[i] -= 1
                        break
                # 만약 다 짝수라면...2빼고는 다 -1을 해주자
                else:
                    for i in range(N):
                        if lst[i] % 2 == 0 and lst[i] > 2:
                            lst[i] -= 1
                            break
        # 짝수날이면
        else:
            # 딱 2인애가 있다면
            for i in range(N):
                if lst[i] == 2:
                    lst[i] -= 2
                    break
            # 딱 2인애가 없으면, 짝수부터 바꿔주기
            else:
                for i in range(N):
                    if lst[i] % 2 == 0 and lst[i] > 0:
                        lst[i] -= 2
                        break
                # 다 홀수가 남았다면, 1보다 큰애들은 빼주자
                else:
                    for i in range(N):
                        if lst[i] % 2 and lst[i] > 1:
                            lst[i] -= 2
                            break

    print(f'#{tc} {day}')

# 이게 되네
# 진짜 무식하게 풀었녜ㅣ,,,






# # goal이 홀수일 때,
# def mul1(namu, level):
#     # 종료조건
#     if sum(namu) == goal * N:
#         return level
    
#     level += 1
#     # 홀수번째 날
#     if level % 2:
#         for i in range(N):
#             # goal이 아니고, 짝수라면
#             if namu[i] < goal and namu[i] % 2 == 0:
#                 namu[i] += 1
#                 return mul1(namu, level)
#         else:   #없다면
#             for i in range(N):
#                 if goal - namu[i] > 3:
#                     namu[i] += 1
#                     return mul1(namu, level)
#             return mul1(namu, level)
#     # 짝수번째 날
#     else:
#         for i in range(N):
#             # goal이 아니고, 홀수라면
#             if namu[i] < goal and namu[i] % 2:
#                 namu[i] += 2
#                 return mul1(namu,level)
#         else:
#             for i in range(N):
#                 if goal - namu[i] > 3:
#                     namu[i] += 2
#                     return mul1(namu, level)
#             return mul1(namu, level)


# # goal이 짝수일 때,
# def mul2(namu, level):
#     # 종료조건
#     if sum(namu) == goal * N:
#         return level
    
#     level += 1
#     # 홀수번째 날
#     if level % 2:
#         for i in range(N):
#             # goal이 아니고, 홀수라면
#             if namu[i] < goal and namu[i] % 2:
#                 namu[i] += 1
#                 return mul2(namu, level)
#         else:   #없다면
#             for i in range(N):
#                 if goal - namu[i] > 3:
#                     namu[i] += 1
#                     return mul2(namu, level)
#             return mul2(namu, level)
#     # 짝수번째 날
#     else:
#         for i in range(N):
#             # goal이 아니고, 짝수라면
#             if namu[i] < goal and namu[i] % 2 == 0:
#                 namu[i] += 2
#                 return mul2(namu,level)
#         else:
#             for i in range(N):
#                 if goal - namu[i] > 3:
#                     namu[i] += 2
#                     return mul2(namu, level)
#             return mul2(namu, level)



# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     namu = list(map(int,input().split()))
#     goal = max(namu)
#     if goal % 2:
#         ans = mul1(namu,0)
#     else:
#         ans = mul2(namu,0)
#     print(f'#{tc} {ans}')
