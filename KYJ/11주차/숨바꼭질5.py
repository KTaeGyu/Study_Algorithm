'''
8725 328744
-1

27297 339652
425

34768 292340
-1

438 129118
95

4040 160532
385
'''
# import heapq

# def find(n, k):
#     pq = []
#     heapq.heappush(pq, (0, n, k)) # 레벨, 현재 위치, 목표
#     check = [0 for _ in range(500001)]
#     minlevel = float('INF')

#     while pq:
#         level, now, goal = heapq.heappop(pq)
#         goal += level
#         # print(f'차이 = {cha}, level = {level}, 현재위치={now}, 목표= {goal}')
#         if now == goal and level < minlevel:
#             minlevel = level
#         if now == goal and level > minlevel:
#             return minlevel
        
#         # 가지치기 1. goal이 범위를 넘어갈때
#         if goal > 500000:
#             return -1
        
#         if check[now] == 0:
#             for next in [now + 1, now - 1, 2 * now]:
#                 if 0 < next <= 500000:
#                     heapq.heappush(pq, (level + 1, next, goal))
#         # 왔다갔다(짝수일때만?)
#         check[now] = 1
#         heapq.heappush(pq, (level + 2, now, goal))

#     return -1


# N, K = map(int,input().split())
# print(find(N,K))





'''
짝수초에 방문한 점을 동생이 짝수초에 지나간다면, 찾은 것이라고 할 수 있고
홀수도 똑같다
'''

from collections import deque

def find(n, k):
    que = deque([(n, 0, k)])   # 현재 위치, 레벨
    # 언니가 짝수/ 홀수 초에 방문한 곳 
    even = [0]*500001
    odd = [0]*500001

    while que:
        now, level, goal = que.popleft()
        # print(now,level,goal)

        # 가지치기 1. goal이 범위를 넘어갈때
        if goal > 500000:
            return -1
        

        if now == goal:
            return level  

        if level % 2:
            if odd[goal]:
                return level
        else:
            if even[goal]:
                return level
    
        if level % 2 == 0:
            for next in [2 * now, now + 1, now - 1]:
                if 0 < next <= 500000:
                    if odd[next] == 0:
                        odd[next] = level + 1
                        que.append((next, level + 1, goal + level + 1))
        else:
            for next in [2 * now, now + 1, now - 1]:
                if 0 <= next <= 500000:
                    if even[next] == 0:
                        even[next] = level + 1
                        que.append((next, level + 1, goal + level + 1))
                    
    return -1


N, K = map(int,input().split())
print(find(N,K))


# '''
# 짝수 후보랑 홀수 후보를 미리 만들어 놓을까?
# '''


# from collections import deque

# def find(n, k):
#  

#     que = deque([(n, 0, k)])   # 현재 위치, 레벨, 목표
#     evenlst = []
#     oddlst = []
#     i = 0
#     num = k
#     while 0 < num <= 500000:
#         i += 1
#         num += i
#         if i % 2:
#             oddlst.append(num)
#         else:
#             evenlst.append(num)

#     # print(len(evenlst), len(oddlst))

#     while que:
#         now, level, goal = que.popleft()
#         goal += level
#         # print(now, level, goal)
#         if now == goal:
#             return level

#         if now > goal:
#             if level % 2:
#                 for i in range(len(oddlst)):
#                     if now == oddlst[i]:
#                         return 2 * (i+1) + 1
#             else:
#                 for i in range(len(evenlst)):
#                     if now == evenlst[i]:
#                         return 2 * (i+1)
                
        
#         # 가지치기 1. goal이 범위를 넘어갈때
#         if goal > 500000:
#             return -1
        
#         # 가지치기 2. goal이 현재보다 2배 이상 클때
#         # if goal >= now * 2:
#         #     next = now * 2
#         #     que.append((next, level + 1, goal))
#         else:
#             for next in [2 * now, now + 1, now - 1]:
#                 if 0 < next <= 500000:
#                     que.append((next, level + 1, goal))
#     return -1


# N, K = map(int,input().split())
# print(find(N,K))

