"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

첫째 줄에 연결 요소의 개수를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

N, M = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
v = set()
cnt = 0
for i in range(1, N+1):
    if i not in v:
        cnt += 1
        s = [i]
        v.add(i)
        while s:
            n = s.pop()
            for j in graph[n]:
                if j not in v:
                    v.add(j)
                    s.append(j)
print(cnt)

"""
6 5
1 2
2 5
5 1
3 4
4 6

2
"""