# 2164번 카드2
# import sys

# n = int(sys.stdin.readline())

# cards = list(range(1, n + 1))

# while len(cards) > 1:
#     dis_card = cards.pop(0)
#     front_card = cards.pop(0)
#     cards.append(front_card)

# print(cards[0])

# 값은 나오는데 시간초과 -> 덱을 이용해보기로

import sys
from collections import deque # 덱이용하려면 써야댐

n = int(sys.stdin.readline())

cards = deque() # 비어있는 덱 생성

for i in range(1, n+1):
    cards.append(i) # 덱에 1부터 n까지 채워넣고

while len(cards) > 1: 
    cards.popleft() # 제일 앞에 꺼 없앰
    dis = cards.popleft() # 앞에 꺼 한번 더 지우고 저장
    cards.append(dis) # 두번째에 지운거 뒤에 넣어줌

num = (list(cards))
print(int(num[0]))
