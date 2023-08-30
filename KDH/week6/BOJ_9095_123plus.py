T = int(input())
DP = [0] * 12
DP[1] = 1
DP[2] = 2
DP[3] = 4
DP[4] = 7
for tc in range(T):
    n = int(input())
    if n >= 5:
        for i in range(5, n+1):
            DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
    print(DP[n])
'''
11111111
-1개
2111111
1211111
-7개
221111
-15개
22211
-10개
2222
-1개
311111
-6개
32111
-10개
3221
-12개
3311
-6개
332
-3개


'''