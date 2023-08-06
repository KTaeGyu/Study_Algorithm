# 11650번 좌표정렬하기

# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬하는 프로그램을 작성하시오.


N = int(input())
nums = [tuple(map(int,input().split())) for _ in range(N)]
nums.sort()

for i in nums:
    print(*i)

# 정렬이 여러가지가 있는데 sort의 시간복잡도가 nlogn이라고 해서 sort사용
# 처음에 튜플이 아니라 list로 받았더니 y좌표는 계산이 안됨