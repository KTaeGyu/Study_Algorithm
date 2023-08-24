N = int(input())
arr = list(map(int, input().split()))
cnt = 1
cnt2 = 1
dp = [1] * N
dp2 = [1] * N
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
        dp[i] = cnt
    elif arr[i] > arr[i+1]:
        cnt = 1
        dp[i] = 1

for i in range(N-1):
    if arr[i] >= arr[i+1]:
        cnt2 += 1
        dp2[i] = cnt2
    elif arr[i] < arr[i+1]:
        cnt2 = 1
        dp2[i] = 1
a = max(dp)
b = max(dp2)

print(max(a, b))