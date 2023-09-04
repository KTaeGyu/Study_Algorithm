import sys
sys.stdin = open("../test.txt", "r")

N = int(input())
con = [[-1, -1]]
for n in range(N):
    s, e = map(int, input().split())
    con.append([s, e])
con.sort(key=lambda x: (x[1], x[0]))
c = list(zip(*con))
cnt = 0
dp = [-1] * (N+1)
for i in range(1, N+1):
    if dp[i-1] <= c[0][i]:
        dp[i] = c[1][i]
        cnt += 1
    else:
        dp[i] = dp[i-1]
print(cnt)



# s = deque([con[0]])
# i = 1
# cnt = 1
# while s:
#     now = s.pop()
#     for j in range(i, N):
#         if con[j][0] >= now[1]:
#             s.append(con[j])
#             i = j
#             cnt += 1
#             break
# print(cnt)
