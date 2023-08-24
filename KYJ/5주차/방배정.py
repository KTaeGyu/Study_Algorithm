# 방 배정

'''
남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 
또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 
물론 한 방에 한 명만 배정하는 것도 가능하다.
한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.
'''

N, K = map(int, input().split())
stu = [[0, 0] for _ in range(6)]
for _ in range(N):
    gen, grade = map(int, input().split())      
    stu[grade - 1][gen] += 1        # 2차원 배열에 몇명인지 넣어주기

cnt = 0
for i in range(6):
    for j in range(2):
        if 0 < stu[i][j] <= K:      # 1 ~ 최대값 사이면 갯수 + 1개
            cnt += 1
        elif stu[i][j] == 0:        # 없으면 패스
            pass
        else:                       # 최대값보다 클 때,
            if stu[i][j] % K:       # 딱떨어지지 않는다면
                cnt += stu[i][j] // K   # 몫 + 1개 더
                cnt += 1
            else:                   # 아니면 몫
                cnt += stu[i][j] // K
print(cnt)
print(stu)