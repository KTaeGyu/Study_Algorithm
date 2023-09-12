"""
1167. 트리의 지름

트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

첫째 줄에 트리의 지름을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

# 2트 가장 먼 거리의 가장 먼 거리 개념 + 기록 방식 변경 (ㅈㄴ어렵네)
V = int(input())
graph = [[] for _ in range(V+1)]
for v in range(V):
    edges = list(map(int, input().split()))
    node = edges[0]
    for i in range(1, len(edges)-1, 2):
        graph[node].append([edges[i], edges[i+1]])


def dfs(n, d):
    for m, f in graph[n]:
        if v[m] == -1:
            v[m] = d + f
            dfs(m, v[m])


v = [-1 for _ in range(V+1)]
v[1] = 0

dfs(1, 0)
s = v.index(max(v))
v = [-1 for _ in range(V + 1)]
v[s] = 0
dfs(s, 0)
print(max(v))

''' 1트 dfs
V = int(input())
graph = {}
for i in range(1, V+1):
    graph[i] = []
for v in range(V):
    edges = list(map(int, input().split()))
    i = 1
    while True:
        now = edges[i]
        if now == -1:
            break
        distance = edges[i+1]
        graph[edges[0]].append((now, distance))
        i += 2
max_r = 0
v = []


def dfs(now, total):
    global max_r
    if max_r < total:
        max_r = total
    v.append(now)
    for nxt, dist in graph[now]:
        if nxt not in v:
            total += dist
            dfs(nxt, total)
            total -= dist


for i in range(1, V+1):
    dfs(i, 0)

print(max_r)
'''

"""
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

11
"""