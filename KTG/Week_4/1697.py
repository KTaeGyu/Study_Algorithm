"""
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
"""
from collections import deque


def BFS(start, end):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        now, level = queue.popleft()
        if now == end:
            return level
        if now not in visited:
            visited.add(now)
            if now - 1 >= 0:
                queue.append((now - 1, level + 1))
            if now + 1 <= 100000:
                queue.append((now + 1, level + 1))
            if now * 2 <= 100000:
                queue.append((now * 2, level + 1))


N, K = map(int, input().split())
print(BFS(N, K))

"""풀이 과정
처음엔 now - 1 의 범위를 잘못 설정하여 queue의 요소가 너무 많이 들어가게 되어 메모리 용량 초과가 났음.
"""
"""
5 17

4
"""