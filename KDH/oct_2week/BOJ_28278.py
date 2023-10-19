# def add_n(x):
#     global stack
#     stack.append(x)
# def st(num):
#     if num == 2:
#         if stack:
#             ans = stack.pop()
#             print(ans)
#         else:
#             print(-1)
#     elif num == 3:
#         print(len(stack))
#     elif num == 4:
#         if stack:
#             print(0)
#         else:
#             print(1)
#     elif num == 5:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)


# sys  안쓰면 시간초과
# sys 안쓰고 푸신분...?

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    # strip으로 공백제거 안하면 2줄로 나뉘어져서 나옴
    num = input().strip()
    if 1 < len(num):
        num = list(num.split())
        num = num.pop()
        stack.append(num)
    else:
        num = int(num)
        if num == 2:
            if stack:
                ans = stack.pop()
                print(ans)
            else:
                print(-1)
        elif num == 3:
            print(len(stack))
        elif num == 4:
            if stack:
                print(0)
            else:
                print(1)
        elif num == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
