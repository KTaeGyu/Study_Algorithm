N = int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(1, N + 1):
    cnt = 0
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x + i][y + j] = 1
    for i in range(101):
        for j in range(101):
            if arr[i][j] == 1:
                cnt += 1
print(cnt)