T = int(input())
for k in range(T):
    n = int(input())
    fb = [[1, 0], [0, 1]]*(n+1)
    for i in range(2, n+1):
        fb[i] = [fb[i-1][0] + fb[i-2][0], fb[i-1][1] + fb[i-2][1]]
    print(*fb[n])
