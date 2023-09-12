
N = int(input())
arr = list(map(int, input().split()))

n_arr = arr
s_arr = list(sorted(set(arr)))
for i in arr:
    print(s_arr.index(i), end=' ')
