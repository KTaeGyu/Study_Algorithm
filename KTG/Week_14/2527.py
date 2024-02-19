for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
    elif p1 == x2:
        if q1 == y2 or y1 == q2:
            print('c')
        else:
            print('b')
    elif q1 == y2:
        if p1 == x2 or x1 == p2:
            print('c')
        else:
            print('b')
    elif x1 == p2:
        if q1 == y2 or y1 == q2:
            print('c')
        else:
            print('b')
    elif y1 == q2:
        if x1 == p2 or p1 == x2:
            print('c')
        else:
            print('b')
    else:
        print('a')