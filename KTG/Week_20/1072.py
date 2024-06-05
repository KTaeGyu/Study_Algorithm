import sys
sys.stdin = open('../test.txt', 'r')

X, Y = map(int, input().split())
Z = (100 * Y) // X
left = 0
right = X
ans = X

if Z >= 99:
    print(-1)
    exit()

while left <= right:
    mid = (left + right) // 2
    percentage = (100 * (Y + mid)) // (X + mid)

    if percentage > Z:
        ans = mid
        right = mid - 1

    else:
        left = mid + 1

print(ans)