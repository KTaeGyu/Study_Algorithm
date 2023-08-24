N, K = map(int, input().split())

people_age = [[] for _ in range(7)]

for _ in range(N):
    S, age = map(int, input().split())
    people_age[age].append(S)

total = 0

for i in people_age:
    one_cnt = i.count(1)
    zero_cnt = i.count(0)
    if one_cnt != 0 and zero_cnt != 0:
        if one_cnt % K != 0 and zero_cnt % K != 0:
            total += (one_cnt // K + 1) + (zero_cnt // K + 1)
        elif one_cnt % K == 0 and zero_cnt % K != 0:
            total += (one_cnt // K) + (zero_cnt // K + 1)
        elif one_cnt % K != 0 and zero_cnt % K == 0:
            total += (one_cnt // K + 1) + (zero_cnt // K)
        else:
            total += (one_cnt // K) + (zero_cnt // K)
    elif one_cnt == 0:
        if zero_cnt % K != 0:
            total += (zero_cnt // K + 1)
        else:
            total += zero_cnt // K
    elif zero_cnt == 0:
        if one_cnt % K != 0:
            total += (one_cnt // K + 1)
        else:
            total += one_cnt // K

print(total)