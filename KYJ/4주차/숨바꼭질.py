# 1697번 숨바꼭질
'''
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하세요
첫줄에 수빈이 위치 N과 동생 위치 K가 주어진다.

[input]
5 17

[output]
4


BFS를 이용해서 풀었다.
if문에서 어려워서 구글링해서 품
min값을 너무 크게 주거나, visited랑 다르게 주면 오류남

'''





from collections import deque

N, K = map(int, input().split())
visited = [0] * 1000001     # 확인 + 경로길이 체크용

def find(n):
    que = deque([n])        # 출발지가 들어있는 큐생성
    visited[n] = 1          # 처음 지점 지난 걸 표시
    min = 1000000           # 무한 루프를 막기 위한 최대값
    while que:
        now = que.popleft()
        if now == K:        # 목표치를 찾으면 멈추고, 길이를 출력 
            return visited[now] - 1
        for nx in (now - 1, now + 1, now * 2):  # if문을 이렇게 쓰는 방법을 몰라서 오래걸림..
            if 0 <= nx < min and visited[nx] == 0:  # 0보다는 크거나 같고, 최대값보다 클 때
                visited[nx] = visited[now] + 1
                que.append(nx)

print(find(N))
