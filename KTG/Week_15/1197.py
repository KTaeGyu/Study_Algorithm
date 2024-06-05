import sys
sys.stdin = open("../test.txt", "r")


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if x > y:
        parents[x] = y
    else:
        parents[y] = x
    return True


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parents = [i for i in range(V + 1)]

edges.sort(key=lambda x: x[2])
ans = 0
for a, b, c in edges:
    if union(a, b):
        ans += c

print(ans)
