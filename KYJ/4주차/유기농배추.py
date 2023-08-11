# 1012번 유기농배추




# 재귀 리미트 생성(없으니까 런타임 에러뜸)
import sys
sys.setrecursionlimit(10000)

T = int(input())    

for tc in range(T):
    M, N, K = map(int, input().split())     # 가로길이, 세로길이, 위치의 갯수
    adj_m = [[0] * M for _ in range(N)]     # 배추 심겨져 있으면 1, 없으면 0 만들기 위한 행렬

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]    # 상하좌우로만 움직일 수 있으므로 방향리스트를 만들어줌

    for _ in range(K):                          # 배추 위치를 받아와서 있는 곳에 1을 해줌
        x, y = map(int, input().split())
        adj_m[y][x] = 1
    
    
    cnt = 0             # 지렁이 마리수

    def DFS(a, b):  # (a, b) 찾기 시작한 점

        for dx, dy in dir:
            nb = b + dx     # (a, b) 기준으로 상하좌우 점 확인해서
            na = a + dy
            if 0 <= na <= (M - 1) and 0 <= nb <= (N - 1):   # 구간안에 있으면서
                if adj_m[nb][na] == 1:      # 배추가 있다면
                    adj_m[nb][na] = -1      # 그리고 지나간거 체크용으로 -1을 해줌
                    DFS(na, nb)         # 그 위치에서 또해줌
            # 그래서 DFS를 한번 돌리면 그 지점에 있는 배추들은 1에서 다 -1이 됨

    for i in range(N):
        for j in range(M):
            if adj_m[i][j] == 1:
                DFS(j, i)
                cnt += 1    # 여기서 돌아간 DFS함수의 갯수 == 지렁이 갯수
 
    print(cnt)


'''
지금까지 푼 DFS + 방향배열

대충 컨셉은 생각이 떠올르는데 구현하는게 너무 어려웠음.
DFS방식을 제대로 이해하고 사용해야할듯
지금까지 배운거 그대로 옮겨쓰려니까 자꾸 삑나서 어려웠다
cnt를 세어주는 위치를 정하는 것도 헷갈렸다
'''





















# T = int(input())

# for tc in range(T):
#     M, N, K = map(int, input().split())
#     arr = []
#     for _ in range(K):
#         a1, a2 = map(int,input().split())
#         arr.append(a1)
#         arr.append(a2)

#     adj_m = [[0] * M] * N 
#     for i in range(K):
#         v1, v2 = arr[2 * i], arr[2 * i + 1]
#         adj_m[v2][v1] = 1
    
#     visited = [[0] * M] * N 
#     dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     cnt = 0

#     def DFS(a,b):       # (a, b)는 출발점
#         global cnt
#         stack = []
#         stack.append((b,a))
#         visited[b][a] += 1

#         while True:
#             for dx, dy in dir:
#                 nb = b + dx
#                 na = a + dy
#                 if 0 <= nb <= (M - 1) and 0 <= na <= (N - 1):
#                     if adj_m[nb][na] == 1 and visited[nb][na] == 0:
#                         stack.append((nb,na))
#                         visited[na][nb] = 1
#                         b, a = nb, na
#                         break
#             else:
#                 if stack:
#                     a, b = stack.pop()
#                 else:
#                     cnt += 1
#                     break


#     def fun():
#         for i in range(N):
#             for j in range(M):
#                 if visited[i][j] != 0:
#                     DFS(i,j)      

    
#     DFS(0,0)
#     fun()

#     print(cnt)