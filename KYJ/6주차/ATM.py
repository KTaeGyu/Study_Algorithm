# ATM

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
for i in range(N):
    result += arr[i] * (N - i)
print(result)


# 이게 왜 맞지..
