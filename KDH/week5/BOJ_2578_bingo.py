bingo = [list(map(int, input().split())) for _ in range(5)]
# for _ in range(5):
#     num_list = list(map(int,input().split()))
#     test.extend(num_list)

speak = [list(map(int, input().split())) for _ in range(5)]

c_cnt = 0
flag = 0
for i in range (5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if speak[i][j] == bingo[k][l]:
                    bingo[k][l] = 0
        c_cnt += 1
        cnt = 0
        for m in range(5):
            if sum(bingo[m]) == 0:
                cnt += 1
            sero = []
            for n in range(5):
                sero.append(bingo[n][m])
            if sum(sero) == 0:
                cnt += 1

        dae1 = []
        for o in range(5):
            dae1.append(bingo[o][o])
        if sum(dae1) == 0:
            cnt += 1
        dae2 = []
        for p in range(5):
            dae2.append(bingo[(-p)-1][p])
        if sum(dae2) == 0:
            cnt += 1
        if cnt >= 3:
            print(c_cnt)
            flag = 1
            break
    if flag == 1:
        break

