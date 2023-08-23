## SWea 종이붙이기

T = int(input())

def paper(n):
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else:
            return paper(n - 20) * 2 + paper(n - 10)
  
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {paper(N)}')

