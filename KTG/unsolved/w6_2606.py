import sys
sys.stdin = open("../test.txt", "r")

N = int(input())
M = int(input())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
v = set()
s = [1]
v.add(1)
while s:
    now = s.pop()
    for j in graph[now]:
        if j not in v:
            v.add(j)
            s.append(j)
            cnt += 1
print(cnt)
