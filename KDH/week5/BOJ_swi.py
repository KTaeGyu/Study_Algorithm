def b_swi(num):
        a = num
        while num <= len(switch):
            if switch[num - 1] == 1:
                switch[num - 1] = 0

            elif switch[num - 1] == 0:
                switch[num - 1] = 1
            num += a


def g_swi(num):
    a = min(num, (N+1)- num)
    for i in range(a):
        if switch[(num-1)-i] == switch[(num-1) + i]:
            if switch[(num-1)-i] == 1:
                switch[(num-1)-i] = 0
                switch[(num-1)+i] = 0
            else:
                switch[(num-1) - i] = 1
                switch[(num-1) + i] = 1
        else:
            break


N = int(input())
switch = list(map(int, input().split()))
hak = int(input())
n_list = []
for _ in range(hak):
    sex, num = map(int, input().split())
    n_list.append([sex, num])
for i in range(hak):
    if n_list[i][0] == 1:
        b_swi(n_list[i][1])
    elif n_list[i][0] == 2:
        g_swi(n_list[i][1])
for i in range(0, len(switch), 20):
    print(*switch[i:i+20])
