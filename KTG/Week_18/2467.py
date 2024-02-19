N = int(input())
arr = list(map(int, input().split()))
minimum = float("inf")
i, j, X, Y = 0, 1, 0, -1

while arr[i] != arr[-j]:
    my_sum = arr[i] + arr[-j]
    if minimum > abs(my_sum):
        minimum = abs(my_sum)
        X, Y = i, -j
    if arr[i] == arr[-j-1]:
        break
    if my_sum <= 0:
        i += 1
    elif my_sum > 0:
        j += 1

print(arr[X], arr[Y])