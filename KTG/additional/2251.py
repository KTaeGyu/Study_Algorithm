import sys
sys.stdin = open("input.txt", "r")
from collections import deque

A, B, C = map(int, input().split())
q = deque()
q.append((0, 0, C))
visited = {q[0]}
result = set()
while q:
    a, b, c = q.popleft()
    if a == 0:
        result.add(c)
    nxt = []
    if a > 0:
        if b < B:
            if a > B - b:
                nxt.append((a - (B - b), B, c))
            elif a <= B - b:
                nxt.append((0, b + a, c))
        if c < C:
            if a > C - c:
                nxt.append((a - (C - c), b, C))
            elif a <= C - c:
                nxt.append((0, b, c + a))
    if b > 0:
        if a < A:
            if b > A - a:
                nxt.append((A, b - (A - a), c))
            elif b <= A - a:
                nxt.append((a + b, 0, c))
        if c < C:
            if b > C - c:
                nxt.append((a, B - (C - c), C))
            elif b <= C - c:
                nxt.append((a, 0, c + b))
    if c > 0:
        if a < A:
            if c > A - a:
                nxt.append((A, b, c - (A - a)))
            elif c <= A - a:
                nxt.append((a + c, b, 0))
        if b < B:
            if c > B - b:
                nxt.append((a, B, c - (B - b)))
            elif c <= B - b:
                nxt.append((a, b + c, 0))
    for i in nxt:
        if i not in visited:
            visited.add(i)
            q.append(i)
ans = list(result)
ans.sort()
print(*ans)
