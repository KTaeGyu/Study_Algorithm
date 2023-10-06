# 문제

# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
# 입력

# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 
# 출력

# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
# 제한

#     2 ≤ K ≤ 5
#     1 ≤ V ≤ 20,000
#     1 ≤ E ≤ 200,000

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1  
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            # 아직 방문하지 않은 노드라면
            if visited[i] == 0:
                # 이전 노드의 반대 값을 지정 (-1 또는 1)
                visited[i] = -visited[node]
                queue.append(i)
            # 인접 노드와 현재 노드의 값이 같다면 이분 그래프가 아님
            elif visited[i] == visited[node]:
                return False
    return True

K = int(input())  
for _ in range(K):
    V, E = map(int, input().split())  
    graph = [[] for _ in range(V + 1)]  
    visited = [0] * (V + 1)  
 
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  

    is_bipartite = True  # 이분 그래프 판별 변수
    for i in range(1, V + 1):
        # 방문하지 않은 정점에 대해서만 bfs 수행
        if visited[i] == 0:
            if not bfs(graph, i, visited):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")