# 11050번 이항계수1

# nCk값 구하기
n, k = map(int,input().split())

# 분자(numerator)는 n부터 k개를 -1씩 해가면서 곱하고
# 분모(denominator)는 k부터 1까지 곱함

# 분자부터 구해보자
numer = 1 
for i in range(k):
    numer = numer * (n-i)

# 분모는

demo = 1
for j in range(2, k+1):
    demo = demo * j

print(int(numer / demo))

