# 1629번 곱셈
'''
자연수 A를 B번 곱한 수를 알고 싶다. 
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 
구하는 프로그램을 작성하시오.

[입력]
10 11 12

[출력]
4
'''

a, b, c = map(int,input().split())

def multi(a, b, c):        
    if b == 1 or b == 0:
        return (a ** b) % c
    else:
        if b % 2:   # b가 홀수라면,
            return (a * multi(a, b // 2, c) ** 2) % c
        else:
            return (multi(a, b // 2, c) ** 2) % c

print(multi(a,b,c))
