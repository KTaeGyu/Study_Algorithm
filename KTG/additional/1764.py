N, M = map(int, input().split())
people = set()
for n in range(N):
    people.add(input())
result = []
ans = 0
for m in range(M):
    person = input()
    if person in people:
        result.append(person)
        ans += 1
print(ans)
print(*sorted(result), sep='\n')
