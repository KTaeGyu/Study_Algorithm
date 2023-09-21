"""
1865: 웜홀

때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
(단 도로는 방향이 없으며 웜홀은 방향이 있다.) 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데,
특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때,
출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500),
도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다.
그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다.
S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다.
그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데 S는 시작 지점,
E는 도착 지점, T는 줄어드는 시간을 의미한다. T는 10,000보다 작거나 같은 자연수 또는 0이다.

두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.
"""
import sys
sys.stdin = open("../test.txt", "r")

# 벨만-포드 공부 후 작성
# 벨만-포드 알고리즘은, N개의 노드에 M개의 간선이 있을 때 사용한다.
# 정상적인 그래프에서는 모든 간선(M)을 N-1번 순회하면 최소값을 찾을 수 있다는 개념을 응용한 것이다.
# 즉, N번째 순회에서 값이 갱신된다면, 해당 그래프는 음수 사이클을 갖는다고 볼 수 있다.
T = int(input())
for tc in range(1, T+1):
    # 입력 데이터 정리
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]  # 인접그래프(간선)
    for _ in range(M):  # 도로
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):  # 웜홀
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    # 초기값
    distance = [10001 for _ in range(N+1)]  # 백준은 쓰래기다.
    distance[1] = 0
    # 음수사이클 판별 flag
    flag = 0
    # 최소값 갱신 사이클
    for cycle in range(1, N+1):
        for node in range(1, N+1):
            for edge, weight in graph[node]:
                if distance[edge] > distance[node] + weight:
                    distance[edge] = distance[node] + weight
                    if cycle == N:  # 음수사이클 판별 로직
                        flag = 1
                        break
            if flag: break
        if flag: break
    # 출력
    print('YES' if flag else 'NO')

""" 각 엣지마다 방문기록을 남겨보았으나 실패
def solve(fn, i, j, t):
    v[i][j] = 1
    n = graph[i][j][1]
    if n == fn and t < 0:
        global flag
        flag = 1
    for nj in range(len(graph[n])):
        if not v[n][nj]:
            nt = graph[n][nj][0]
            solve(i, n, nj, t+nt)


T = int(input())
for tc in range(1, T + 1):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for m in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((T, E))
        graph[E].append((T, S))
    for w in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((-T, E))
    visited = []
    for i in range(N+1):
        visited.append([])
        for j in graph[i]:
            visited[i].append(0)
    ans = 'NO'
    for i in range(1, N + 1):
        for j in range(len(graph[i])):
            v = deepcopy(visited)
            flag = 0
            solve(i, i, j, graph[i][j][0])
            if flag:
                ans = 'YES'
    print(ans)
"""
""" 풀이1: 각 노드마다 방문기록을 표시 / 문제점: 원형구조를 거쳐 음수가 되는 경우 불가능 
def solve(t, i, n):
    visited[n] = 1
    if n == i and t < 0:
        global flag
        flag = 1
    for nt, nn in graph[n]:
        if not visited[nn]:
            solve(t + nt, i, nn)


ans = 'NO'
for i in range(1, N + 1):
    for t, n in graph[i]:
        visited = [0] * (N + 1)
        flag = 0
        solve(t, i, n)
        if flag:
            ans = 'YES'
print(ans)
"""
"""
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8

NO
YES
"""