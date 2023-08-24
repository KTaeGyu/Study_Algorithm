# 경비원
# 각각의 경우를 나눠서 if를 해야하나
'''
[입력]
10 5
3
1 4
3 2
2 8
2 3

[출력]
23
'''

w, h = map(int, input().split())
MAP = [0 for _ in range(2 * (w + h))]
n = int(input())

for i in range(n + 1):
    a, b =  map(int, input().split())
    if a == 1:
        MAP[b] = i + 1
    elif a == 2:
        MAP[w + h + (w - b)] = i + 1
    elif a == 3:
        MAP[w + h + w + (h - b)] = i + 1
    else:
        MAP[w + b] = i + 1

# print(MAP)
# 동그니 위치
loca = MAP.index(n + 1)
# print(loca)

ans = 0      # 최단거리의 합
for j in range(1, n + 1):
    a = MAP.index(j)    # 상점의 인덱스
    # print(a)
    if loca > a:
        dis1 = loca - a
        dis2 = len(MAP) - loca + a 
    else:
        dis1 = a - loca 
        dis2 = len(MAP) - a + loca 
    
    # print(dis1, dis2)
    ans += min(dis1, dis2)

print(ans)

    
