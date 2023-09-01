N = int(input())
time = list(map(int, input().split()))
S = sorted(time)
ans = 0
for i in range(1, N+1):
    ans += (S[-i]*i)
print(ans)