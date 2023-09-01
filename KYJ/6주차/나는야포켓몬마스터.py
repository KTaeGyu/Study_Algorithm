## 1620번 나는야 포켓몬 마스터 이다솜

# N , M = map(int, input().split())

# pocketdic = []
# for i in range(N):
#     pocketdic.append(input())



# problems = [input() for _ in range(M)]

# for problem in problems:
#     if problem.isdecimal():
#         print(pocketdic[int(problem) - 1])
#     else:
#         print(pocketdic.index(problem) + 1)

# 답은 나오는데 시간초과


# 리스트보다 딕셔너리가 시간이 훨 빠름
# 딕셔너리를 이용해서 해보자




N , M = map(int, input().split())
dic1 = {}
dic2 = {}

for i in range(N):
    a = input()
    dic1[i + 1] = a
    dic2[a] = i + 1

problems = [input() for _ in range(M)]

for pro in problems:
    if pro.isdecimal():
        print(dic1[int(pro)])
    else:
        print(dic2[pro])