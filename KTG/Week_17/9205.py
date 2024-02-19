import sys
sys.stdin = open('../test.txt', 'r')
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    cord = [list(map(int, input().split())) for _ in range(n+2)]
    result = 'sad'

    q = deque([cord[0]])
    v = {0}

    while q:
        x, y = q.popleft()
        if abs(x-cord[n+1][0]) + abs(y-cord[n+1][1]) <= 1000:
            result = 'happy'
            break
        for i in range(1, n + 1):
            if i in v:
                continue
            if abs(x - cord[i][0]) + abs(y - cord[i][1]) <= 1000:
                q.append(cord[i])
                v.add(i)

    print(result)