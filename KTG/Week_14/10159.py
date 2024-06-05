N = int(input())
M = int(input())

graph = [[2001] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for i in range(M):
    heavy, light = map(int, input().split())
    graph[heavy][light] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        if graph[i][j] == 2001 and graph[j][i] == 2001:
            cnt += 1
    print(cnt)

# 시도 1: 그리디? (무거운 것보다 무거운것, 가벼운 것보다 가벼운것 계산)
# 처음에 반복을 1회만 해서 틀렸다가
# 플로이드 워셜 알고리즘을 보고 N회 반복하는 것으로 고쳐서 맞음
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(M)]

relations = [[-2] * (N + 1)] + [[-2] + [0] * N for _ in range(N)]

for k in range(1, N+1):
    for i in range(1, N+1):
        for heavy, light in graph:
            if heavy == i:
                relations[heavy][light] = 1
                relations[light][heavy] = -1
                for j in range(1, N+1):
                    if relations[heavy][j] == -1:
                        relations[j][light] = 1
                        relations[light][j] = -1
                    if relations[light][j] == 1:
                        relations[j][heavy] = -1
                        relations[heavy][j] = 1

for i in range(1, N+1):
    print(relations[i].count(0) - 1)