"""
은하는 수업 때 1부터 N까지 수의 합과 1부터 N까지 수의 세제곱의 합과 관련된 다음 공식을 배웠습니다.
    - (1 + 2 + ... + N)^2 = 1^3 + 2^3 + ... + N^3
믿을 수 없었던 은하는 직접 코딩을 해서 검증해 보기로 했습니다. 1부터 N까지 수의 합과 그 수를 제곱한 수,
또 1부터 N까지 수의 세제곱의 합을 차례대로 출력하세요.

첫 줄에 분제의 정수 N 이 주어진다

세 줄을 출력한다.
    - 첫 줄에는 1부터 N까지 수의 합
    - 둘째 줄에는 1부터 N까지 수의 합을 제곱한 수
    - 셋째 줄에는 1부터 N까지 수의 세제곱의 합
"""
N = int(input())
add = 0
for i in range(1, N+1):
    add += i
print(add)
print(add ** 2)
tre = 0
for i in range(1, N+1):
    tre += (i ** 3)
print(tre)

"""

"""