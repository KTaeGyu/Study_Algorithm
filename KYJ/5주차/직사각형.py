# 직사각형

# 상당히 무식하게 풀었다..

def find(sqr1, sqr2):
    # 첫번째로 공통부분이 없을 때
    if sqr1[2] < sqr2[0] or sqr1[3] < sqr2[1]:
        return 'd'
    if sqr2[2] < sqr1[0] or sqr2[3] < sqr1[1]:
        return 'd'
    
    # 둘이 한 점에서 만날 때
    if sqr1[0] == sqr2[2] and sqr1[3] == sqr2[1]:
        return 'c'
    if sqr1[2] == sqr2[0] and sqr1[3] == sqr2[1]:
        return 'c'
    if sqr1[0] == sqr2[2] and sqr1[1] == sqr2[3]:
        return 'c'
    if sqr1[2] == sqr2[0] and sqr1[1] == sqr2[3]:
        return 'c'
    
    # 한직선에서 만날 때
    if sqr1[3] == sqr2[1]:
        if sqr1[0] < sqr2[2] or sqr1[2] > sqr2[0]:
            return 'b'
    if sqr1[1] == sqr2[3]:
        if sqr1[0] < sqr2[2] or sqr1[2] > sqr2[0]:
            return 'b'
    if sqr1[0] == sqr2[2]:
        if sqr1[1] < sqr2[3] or sqr1[3] > sqr2[1]:
            return 'b'
    if sqr1[2] == sqr2[0]:
        if sqr1[1] < sqr2[3] or sqr1[3] > sqr2[1]:
            return 'b' 
    
    # 나머지 경우
    return 'a'



for _ in range(4):  # 테케가 4개
    arr = list(map(int,input().split()))
    sqr1 = arr[:4]
    sqr2 = arr[4:]
    print(find(sqr1, sqr2))
    