import sys
sys.stdin = open('../test.txt', 'r')

N, M = map(int, input().split())
buses = [list(map(int, input().split())) for _ in range(M)]

INF = int(1e9)
table = [INF] * (N + 1)
table[1] = 0

isNegativeCycle = 0
for i in range(N):
    for j in range(M):
        A, B, C = buses[j]
        if table[A] != INF and table[A] + C < table[B]:
            table[B] = table[A] + C
            if i == N - 1:
                isNegativeCycle = 1

if isNegativeCycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if table[i] == INF:
            print(-1)
        else:
            print(table[i])
