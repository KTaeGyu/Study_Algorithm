# baby - gin 게임
# 0~9까지의 카드에서 6장을 뽑았을 때, 연속하는게 triple, 같은 숫자 3개가 어쩌고
# 그랬을때 그걸로만 이루어진 경우를 baby - gin이라고 한다
# 판별하는 방법은?

cards = list(map(int,input().split()))

count = [0] * (max(cards) + 1)

for i in cards:
    count[i] += 1

# print(count)
babygin = [0, 0]

for i in range(len(count)):
    if count[i] >= 3:
        babygin[0] += 1
        count[i] -= 3

for i in range(len(count) - 2):
    if count [i] > 0  and count[i+1] > 0 and count[i+2] > 0:
        babygin[1] += 1
        count[i] -= 1
        count[i+1] -= 1
        count[i+2] -= 1

if sum(babygin) == 2:
    print('BabyGin!')
else:
    print('No..')