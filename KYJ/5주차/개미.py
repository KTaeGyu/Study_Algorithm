# 개미
'''
6 4
4 1
8


0 1
'''


w, h =  map(int,input().split())
x, y = map(int,input().split())
t = int(input())


at = t % (2*w)
a = w - x   # 현재위치부터 오른쪽
b = x       # 현재위치부터 왼쪽
if at <= a:
    dx = x + at
elif a < at <= 2 * a:
    dx = w - (at - a)
elif 2 * a < at <= 2 * a + b:
    dx = x - (at - 2 * a)
else:
    dx = at - 2 * a - b 


bt = t % (2*h)
c = h - y   # 현재위치부터 위
d = y       # 현재위치부터 아래쪽
if bt <= c:
    dy = y + bt
elif c < bt <= 2 * c:
    dy = h - (bt - c)
elif 2 * c < bt <= 2 * c + d:
    dy = y - (bt - 2 * c)
else:
    dy = bt - 2 * c - d 
    
print(dx, dy)

