N, M = map(int, input().split())
dogam = {}
for i in range(1, N+1):
    a = input()
    dogam[i] = a
    dogam[a] = i
for i in range(M):
    a = input()
    if a.isdigit():
        a = int(a)
    print(dogam.get(a))