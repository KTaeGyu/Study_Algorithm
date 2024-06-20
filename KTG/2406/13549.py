import sys
sys.stdin = open('./13549.txt', 'r')

from collections import deque

N, K = map(int, input().split())

nodes = [0] * 100001


def bfs(n, k):
    q = deque()
    if n == 0 and k == 0:
        return 0
    elif n == 0:
        q.append(1)
    else:
        q.append(n)

    while q:
        now = q.popleft()
        if k == now:
            if n == 0:
                return nodes[now] + 1
            return nodes[now]
        for nxt in (now - 1, now + 1, now * 2):
            if 100001 > nxt >= 0 == nodes[nxt]:
                if nxt == now * 2:
                    nodes[nxt] = nodes[now]
                    q.appendleft(nxt)
                else:
                    nodes[nxt] = nodes[now] + 1
                    q.append(nxt)


print(bfs(N, K))
