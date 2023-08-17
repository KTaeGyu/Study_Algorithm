# 콜라츠 추측

cnt = 0

def cola(n):
    global cnt
    if n == 1:
        return 1
    elif n % 2 == 0:
        cnt += 1
        return cola(n // 2)
    else:
        cnt += 1
        return cola(3 * n + 1)
    
N = int(input())
cola(N)
print(cnt)