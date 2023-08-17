# DFS를 배웠으니까
# 촌수계산을 이 방식으로 다시


# GPT가 살짝 수정해줌

N = int(input())            # 전체 사람수  
key1, key2 = map(int,input().split())       # 찾아야하는 관계
M = int(input())            # 관계 개수
arr = []                    # 관계들을 하나의 list로 받아둠
for _ in range(M):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
adj_m = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a1 = arr[2 * i]
    a2 = arr[2 * i + 1]
    adj_m[a1][a2] = 1
    adj_m[a2][a1] = 1

def dps(key1, key2, N, adj_m):
    if key1 == key2:
        return 0
    
    stack = []
    visited = [0] * (N + 1)
    visited[key1] = 1
    cnt = 0

    stack.append((key1, cnt))   # stack을 튜플 형태로 구성
    while stack:                # 스택이 비어있지 않을때 까지 
        currnet, cnt = stack.pop()  # 첫번째 요소는 마지막에 저장된 것 가져오기

        for w in range(1, N + 1):   
            if adj_m[currnet][w] == 1 and visited[w] == 0:  # 같은 거 찾고, 방문한 적 없다면
                visited[w] = 1      # 방문 체크해주고
                if w == key2:       # 만약에 목표했던 곳이면
                    result = cnt + 1    # 카운트 세주고 
                    return result       # 몇개 거쳐서 왔는지 출력
                stack.append((w, cnt + 1))  # 스택에 새로운 위치와 카운트+1
    return -1           # 못찾으면 -1

print(dps(key1, key2, N, adj_m))
















# 처음에 푼 코드


# N = int(input())            # 전체 사람수  
# key1, key2 = map(int,input().split())       # 찾아야하는 관계
# M = int(input())            # 관계 개수
# arr = []                    # 관계들을 하나의 list로 받아둠
# for _ in range(M):
#     a, b = map(int, input().split())
#     arr.append(a)
#     arr.append(b)
# adj_m = [[0] * (N + 1) for _ in range(N + 1)]

# for i in range(M):
#     a1 = arr[2 * i]
#     a2 = arr[2 * i + 1]
#     adj_m[a1][a2] = 1
#     adj_m[a2][a1] = 1

# def dps(key, N, adj_m):
#     if key == key2:
#         return 0
    
#     stack = []
#     visited = [0] * (N + 1)
#     visited[key] = 1
#     cnt = 0

#     while True:
#         for w in range(1, N + 1):
#             if adj_m[key][w] == 1 and visited[w] == 0:
#                 stack.append(key)
#                 key = w
#                 cnt += 1
#                 visited[key] = 1
#                 if w == key2:
#                     result = cnt
#                     return result
#                 break
#         else:
#             if stack:
#                 key = stack.pop()
#             else:
#                 break
#     return -1

# print(dps(key1, N, adj_m))