# 이진수로 만들기

def make_binary(n):
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        if n % 2 == 0:
            return make_binary(n // 2)+'0'
        else:
            return make_binary(n // 2)+'1'

n = int(input())     
print(make_binary(n))