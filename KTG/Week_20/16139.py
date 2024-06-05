S = input()
len_S = len(S)


def alpha_to_num(alpha):
    return ord(alpha) - 97


dp = [[0 for _ in range(26)] for _ in range(len_S)]
dp[0][alpha_to_num(S[0])] = 1
for i in range(1, len_S):
    dp[i][alpha_to_num(S[i])] = 1
    for j in range(26):
        dp[i][j] += dp[i - 1][j]

q = int(input())
for i in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)

    if l > 0:
        ans = dp[r][alpha_to_num(a)] - dp[l - 1][alpha_to_num(a)]
    else:
        ans = dp[r][alpha_to_num(a)]

    print(ans)