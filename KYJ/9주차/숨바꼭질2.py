# 12851번 숨바꼭질2
'''
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 
1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 
그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 
구하는 프로그램을 작성하시오.

수빈이 위치 N, 동생 위치 K
5 17

가장 빠른시간, 방법의 수
4
2
'''
'''
BFS


메모리 초과에 시간초과에 난리..
- visited 방문처리를 que에서 꺼내서 해줌
- 가망없는 애들은 쳐내주기
'''

from collections import deque

N, K = map(int,input().split())

q =  deque([(N, 0)])
cnt = 0
minv = float('INF')
visited = [0 for _ in range(100001)]
while q:
    now, level = q.popleft()
    visited[now] = 1 
    if now == K:
        if level < minv:
            minv = level
            cnt = 1
        elif level == minv:
            cnt += 1
    if cnt:
        if level > minv:
            break

    hubo = [now - 1, now + 1, now * 2]
    for i in range(3):
        if now > K and i != 0:
            continue
        if 0 <= hubo[i] <= 100000 and visited[hubo[i]] == 0:
            q.append((hubo[i], level + 1))

print(minv)
print(cnt)