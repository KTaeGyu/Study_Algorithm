"""
1238: 파티

N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.
이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다.
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다.
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")
import heapq


# 트라이3 다익스트라 최적화(힙 이용)
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    A, B, Ti = map(int, input().split())
    graph[A].append((B, Ti))


def dijkstra(s):
    time = [float('inf')] * (N+1)
    time[s] = 0
    h = [(0, s)]
    while h:
        t, n = heapq.heappop(h)
        if t > time[n]:
            continue
        for nn, nt in graph[n]:
            if t + nt < time[nn]:
                time[nn] = t + nt
                heapq.heappush(h, (time[nn], nn))
    return time


ans = 0
for i in range(1, N+1):
    if i == X:
        continue
    iX = dijkstra(i)
    Xi = dijkstra(X)
    ans = max(ans, iX[X] + Xi[i])
print(ans)

""" 트라이2 다익스트라 시간초과

graph = [[float('inf')]*(N+1) for _ in range(N+1)]
for m in range(M):
    A, B, Ti = map(int, input().split())
    graph[A][B] = Ti
for n in range(1, N+1):
    graph[n][n] = 0

result = [[]]
for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    time = graph[i].copy()
    for j in range(N-1):
        nxt = float('inf')
        nid = 0
        for k in range(1, N+1):
            if visited[k] == 0 and nxt > time[k]:
                visited[k] = 1
                nxt = time[k]
                nid = k
        for k in range(1, N+1):
            time[k] = min(time[k], time[nid] + graph[nid][k])
    result.append(time)

ans = [0] * N
for i in range(1, N+1):
    ans[i-1] = result[i][X] + result[X][i]
print(max(ans))
"""

""" 트라이1 DFS 시간초과
def dfs(now, e, t):
    visited[now] = 1
    if now == e:
        global temp
        if temp > t:
            temp = t
    for nxt in range(1, N+1):
        if graph[now][nxt] != 0 and visited[nxt] == 0:
            dfs(nxt, e, t + graph[now][nxt])


for i in range(1, N+1):
    visited = [0] * (N+1)
    temp = float('inf')
    dfs(i, X, 0)
    time[i] += temp
    visited = [0] * (N+1)
    temp = float('inf')
    dfs(X, i, 0)
    time[i] += temp

print(max(time))
"""

"""
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

10
"""