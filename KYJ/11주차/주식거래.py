# SWEA 주식거래
'''
과거 거래 종목들의 데이터가 주어졌을때,
이론상 실현 가능한 최대 수익을 계산하는 프로그램을 작성하라.
매월 보유한 주식은 항상 다음 달에 모두 매도해야 한다.
'''
T = int(input())
for tc in range(1, T  + 1):
    Ms, Ma = map(int,input().split())
    N, L = map(int,input().split())
    info = [list(map(int,input().split())) for _ in range(N)]

    # 현재 잔고
    money = Ms
    # DP[i] = i개월에 산 주식의 이익
    DP = [0 for _ in range(L)]
    for i in range(L):
        money += DP[i - 1]
        # 이득이 나는 항목들의 리스트
        oklst = []
        for k in range(N):
            if info[k][i + 1] - info[k][i] > 0:
                oklst.append((info[k][i + 1] - info[k][i], k))
        # 이득이 나는 애들이 있다면,
        # print(oklst)
        if oklst:
            # 이득이 높은 애부터
            oklst.sort(reverse=True)
            for benefit, maxhangmok in oklst:    
                if info[maxhangmok][i] <= money:
                    # 최대 살수 있는 갯수
                    # print(f'나 지금 {money}원 있어')
                    num = money // info[maxhangmok][i]
                    money -= info[maxhangmok][i] * num  # 산돈
                    # print(f'{i}개월 {num}개 사서 {money}남았어요')
                    DP[i] += info[maxhangmok][i + 1] * num   # 벌돈
        else:
            pass
        money += Ma

    # print(DP)
    finalmoney = money + DP[-1]
    firstmoney = Ms + Ma * L
    result = finalmoney - firstmoney 
    print(f'#{tc} {result}')