import math

num = int(input())

left = 0
right = num
mid = (left + right) // 2
ans = mid

while mid ** 2 != num and left <= right:
    mid = (left + right) // 2

    if mid ** 2 > num:
        right = mid - 1
        ans = mid

    if mid ** 2 < num:
        left = mid + 1

    if mid ** 2 == num:
        ans = mid

print(ans)
