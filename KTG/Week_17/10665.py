import sys
sys.stdin = open('../test.txt' , 'r')

N = int(input())
checkPoints = [list(map(int, input().split())) for _ in range(N)]

dists = []
res = 0
for i in range(N-1):
    dist = abs(checkPoints[i][0] - checkPoints[i+1][0]) + abs(checkPoints[i][1] - checkPoints[i+1][1])
    dists.append(dist)
    res += dist

ans = 1e21
for i in range(1, N-2):
    tem = abs(checkPoints[i-1][0] - checkPoints[i+1][0]) + abs(checkPoints[i-1][1] - checkPoints[i+1][1])
    ans = min(ans, res - dists[i-1] - dists[i] + tem)

print(ans)