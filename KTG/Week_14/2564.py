def position(direction, pos, lst):
    if direction == 1:
        lst.append((0, pos))
    elif direction == 2:
        lst.append((M, pos))
    elif direction == 3:
        lst.append((pos, 0))
    elif direction == 4:
        lst.append((pos, N))


N, M = map(int, input().split())
K = int(input())

# 상점 위치를 1번에, 경비 위치를 2번에 저장
graph = {1: [], 2: []}
for k in range(K):
    news, dp = map(int, input().split())
    position(news, dp, graph[1])
m_news, m_dp = map(int, input().split())
position(m_news, m_dp, graph[2])

result = 0
for y, x in graph[1]:
    if abs(y - graph[2][0][0]) == M:
        result += M + min((x + graph[2][0][1]), ((N - x) + (N - graph[2][0][1])))
    elif abs(x - graph[2][0][1]) == N:
        result += N + min((y + graph[2][0][0]), ((N - y) + (N - graph[2][0][0])))
    else:
        result += abs(y - graph[2][0][0]) + abs(x - graph[2][0][1])
print(result)