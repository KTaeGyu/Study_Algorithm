T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    v = [0] * (n + 1)
    ans = n
    for i in range(1, n+1):
        if not v[i]:
            t = [i]
            now = i
            j = 0
            while True:
                v[now] = 1
                nxt = arr[now]
                if v[nxt]:
                    if nxt in t:
                        ans -= len(t[t.index(nxt):])
                        break
                    break
                t.append(nxt)
                now = nxt
    print(ans)