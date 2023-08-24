# 참외밭

cham = int(input())
ground =[[0 for _ in range(501)] for _ in range(501)]

info = []
for i in range(6):
    dire, l = map(int,input().split())
    info.append([dire, l])

arr = []
# info = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]
for i in range(6):
    if info[i][0]  == info[(i + 2) % 6][0]:    # 현재랑 다다음꺼랑 같은 방향이라면 그 사이꺼가 중간에 낀거니까
        arr.append(info[(i + 1) % 6][1])

small = arr[0] * arr [1]

maxw = 0
maxl = 0
for i in range(6):
    if info[i][0] == 1 or info[i][0] == 2:
        if info[i][1] >= maxl:
            maxl = info[i][1]
    if info[i][0] == 3 or info[i][0] == 4:
        if info[i][1] >= maxw:
            maxw = info[i][1]

print((maxw * maxl - small) * cham)
