# 4153번 직각삼각형

while True:
    a, b, c = map(int,input().split())
    tri = [a, b, c]
    tri.sort()
    if a == 0:
        break
    elif tri[2]**2 == tri[1]**2 + tri[0]**2:
        print('right')
    else:
        print('wrong')