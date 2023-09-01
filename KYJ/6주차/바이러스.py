# 2606번 바이러스
# BFS 연습해보자

'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 
모든 컴퓨터는 웜 바이러스에 걸리게 된다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 
서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하인 양의 정수이고 
각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

[입력]

7
6
1 2
2 3
1 5
5 2
5 6
4 7

[출력]

4
'''

# deque를 쓰기 위해 import
from collections import deque

N = int(input())    # 컴퓨터 개수
nums_node = int(input())       # 노드갯수
nodes = [list(map(int, input().split())) for _ in range(nums_node)]

# 인접행렬 만들어주기
adj = [[0] * (N+1) for _ in range(N+1)]
for i in range(nums_node):
    n = nodes[i][0]  
    m = nodes[i][1] 
    adj[n][m] = 1
    adj[m][n] = 1

# visited 만들기
visited = [0] * (N + 1)

def BFS(start):
    # 큐에 시작점 넣어주고 방문처리
    que = deque([start])
    visited[start] = 1
    cnt = 0
    
    # 큐가 비기 전까지 반복
    while que:
        # 현재 찾고있는 요소 = a
        a = que.popleft()
        for i in range(N + 1):
            if adj[a][i] == 1 and visited[i] == 0:
                # 방문처리 해주고
                visited[i] = 1
                que.append(i)
                cnt += 1
    return cnt

print(BFS(1))
