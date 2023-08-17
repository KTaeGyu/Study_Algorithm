## SWEA 반복문자 지우기
# stack을 이용해 볼까 합니다

T = int(input())

for tc in range(1, T + 1):
    mystr = list(input())
    stack = []
    top = -1
    while True:
        if len(mystr) == len(stack):
            break
        for alpha in mystr:
            if stack and alpha == stack[top]:
                stack.pop()
            else:
                stack.append(alpha)
        mystr = stack
    print(f'#{tc} {len(stack)}')