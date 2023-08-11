# 1074번 Z
'''
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸
순서대로 방문하면 Z모양이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.


[input]
2 3 1

[output]
11
'''


N, r, c = map(int, input().split())
lst = []
cnt = 0

mid = 2 ** (N - 1)
while cnt < N:
    if r >= mid and c >= mid:
        r -= mid
        c -= mid
        a = 3
    elif r >= mid and c < mid:
        r -= mid
        a = 2
    elif r <= mid and c >= mid:
        c -= mid
        a = 1
    else:
        a = 0
    lst.append(a)
    mid = mid // 2
    cnt += 1

lst = lst[::-1]
# print(lst)
ans = 0
for i in range(len(lst)):
    ans += lst[i] * (2 ** (2 * i))

print(ans)

'''
컨셉: 사분면으로 나눠서 어디에 속하는지를 lst에 담고,
lst = [a, b, c]이런식으로 나오면, 
답은 a * (2 ** 2*2) + b * (2 ** 2*1) + c * (2 ** 2*0)
규칙이 있는걸 찾아내서 품
'''