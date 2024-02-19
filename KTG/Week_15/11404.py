import sys
sys.stdin = open("../test.txt", "r")

n = int(input())
m = int(input())

INF = 1e10
fw = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    fw[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    fw[a][b] = min(fw[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if fw[i][j] == INF:
            print("0", end=' ')
            continue
        print(fw[i][j], end=' ')
    print()
