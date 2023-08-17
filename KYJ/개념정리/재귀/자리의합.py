# 자리의 합

def sumnum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumnum(n // 10)
    
print(sumnum(int(input())))