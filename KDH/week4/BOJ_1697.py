from collections import deque

def bfs(start, target):
    visited = [False] * 100001  # 위치의 범위는 0부터 100000까지
    queue = deque([(start, 0)])  # (위치, 시간) 쌍을 저장하는 큐

    while queue:
        position, time = queue.popleft()

        if position == target:
            return time

        if 0 <= position <= 100000 and not visited[position]:
            visited[position] = True
            queue.append((position - 1, time + 1))
            queue.append((position + 1, time + 1))
            queue.append((position * 2, time + 1))

# 입력 받기
N, K = map(int, input().split())

# BFS 실행 및 결과 출력
result = bfs(N, K)
print(result)
