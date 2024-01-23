import sys
sys.stdin = open('../test.txt', 'r')
from collections import deque

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    Ds = [0] + list(map(int, input().split()))

    preBuilding = [[] for _ in range(N + 1)]
    inOrder = [0 for _ in range(N + 1)]
    result = [0 for _ in range(N + 1)]

    for i in range(K):
        X, Y = map(int, input().split())
        preBuilding[X].append(Y)
        inOrder[Y] += 1

    q = deque()
    for i in range(1, N + 1):
        if inOrder[i] == 0:
            q.append(i)
            result[i] = Ds[i]


    while q:
        now = q.popleft()
        for i in preBuilding[now]:
            inOrder[i] -= 1
            result[i] = max(result[i], result[now] + Ds[i])
            if inOrder[i] == 0:
                q.append(i)
    W = int(input())

    print(result[W])
