# A형 기출: 업무처리

# BFS로 풀어야하나..

# 문제를... 잘 읽자....


import copy
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    work = [list(map(int,input().split())) for _ in range(N)]
    # coco[i] = 코코가 i번째 일을 도와줬을 때 걸리는 시간
    coco = [float('inf') for _ in range(N)]
    worktime = [[0 for _ in range(N)] for _ in range(N)]
    is_true = True

    # 총 걸리는 시간은
    def calculate(lst, num):
        global is_true
        cnt = 0
        for i in range(N):
            # 이미 계산된거라면
            if lst[i]:
                continue
            # 선행일이 없다면
            if work_i[i][1] == 0:
                cnt += 1
                lst[i] = work_i[i][0]
            # 선행일이 있다면
            else:
                timelst = []
                flag = True
                for k in work_i[i][2:]:
                    if lst[k - 1] == 0:
                        flag = False
                        pass
                    else:
                        timelst.append(lst[k - 1]) 
                if flag and timelst:
                    cnt += 1
                    lst[i] = max(timelst) + work_i[i][0]
        
        # 만약 이번에 계산이 안되었다면..?
        # 무한루프 방지용 리턴해버림
        if cnt == 0:
            is_true = False
            return
        
        # 시간 계산이 다 안되었다면 다시 돌려주기
        for time in lst:
            if time == 0:
                calculate(lst, cnt)
        else:
            return lst


    for i in range(N):
        # 일하는 시간을 인덱스마다 바꿔서 계산해볼꺼니까 deepcopy
        work_i = copy.deepcopy(work)
        # i번째 일을 도와줬다면
        work_i[i][0] //= 2
        worktime[i] = calculate(worktime[i], 0)
        if worktime[i]:
            coco[i] = max(worktime[i])

    if is_true:
        print(f'#{tc} {min(coco)}')
    else:
        print(f'#{tc} -1')






























# 다시 해볼까

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     is_true = True
#     work = [list(map(int,input().split())) for _ in range(N)]
#     DP = [[0, 0] for _ in range(N)]
#     todolst = [[] for _ in range(N)]

#     # 모두 계산되었는지 확인용
#     check = [1 for _ in range(N)]

#     for i in range(N):
#         # 선행일이 없다면, 
#         if work[i][1] == 0:
#             check[i] = 0
#             # 코코 도움 없음
#             DP[i][0] = work[i][0]
#             # 코코 도움 있음
#             DP[i][1] = work[i][0] // 2
#         # 선행일이 있다면, todolst에 저장
#         else:
#             for k in range(2, len(work[i])):
#                 todolst[i].append(work[i][k] - 1)
    
#     for i in range(N):
#         todolst[i].sort()

#     # 모두가 선행일을 가지고 있음 -> 안댐
#     if sum(check) == N:
#         is_true = False

#     while sum(check):
#         update = False
#         for i in range(N):
#             # 계산되지 않았다면
#             if check[i]:
#                 flag = True
#                 time = [[],[]]
#                 for num in todolst[i]:
#                     # 선행일이 계산이 안되었다면 넘기고
#                     if DP[num][0] == 0:
#                         flag = False
#                         break
#                     else:
#                         time[0].append(DP[num][0])  # 코코 도움 없이
#                         time[1].append(DP[num][1])  # 코코 도움 있음
#                 # 선행일이 모두 계산되었다면, 
#                 if flag:
#                     update = True
#                     # 우선 그냥 쌩으로 한다면 선행일 중에 긴거 + 지금꺼 시간
#                     DP[i][0] = work[i][0] + max(time[0])

#                     # 코코가 도와준다면,
#                     maxtime = 0
#                     for k in range(len(time[1])):
#                         if time[1][k] > maxtime:
#                             # 코코가 도와준 거 중에 제일 긴거
#                             maxtime = time[1][k]
#                             idx = k
#                     temp = 0
#                     # 도와준거 빼고는 원래 값
#                     for j in range(len(time[1])):
#                         if j == idx:
#                             pass
#                         else:
#                             if time[0][j] > temp:
#                                 # 반 줄은거 뺴고 제일 긴거
#                                 temp = time[0][j]
#                     # 이미 한번 도와줬다면
#                     once = max(maxtime, temp) + work[i][0]
#                     # 이번에 도와주는거랑 비교
#                     DP[i][1] = max(once, max(time[0]) + (work[i][0] // 2))
#                     check[i] = 0
#         if not update:
#             is_true = False
#             break
    
#     if is_true:
#         result = 0 
#         for i in range(N):
#             if DP[i][1] > result:
#                 result = DP[i][1]
#                 idx = i
#         for k in range(N):
#             if k == idx:
#                 pass
#             else:
#                 if DP[k][0] > result:
#                     if len(set(todolst[idx]).union(set(todolst[k]))) == len(todolst[idx]) + len(todolst[k]):
#                         result = DP[k][0]
#         print(f'#{tc} {result}')
#     else:
#         print(f'#{tc} -1')