# 1018번 체스판 다시 칠하기


# 긁어옴

n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:   # (짝, 짝) or (홀, 홀)
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
 
print(min(result))




















# n, m = map(int, input().split())

# # input을 list와 str의 형태로 받아줌

# chesslist = []

# for i in range(n):
#     row_list = input()
#     chesslist.append(row_list)


# # print(chesslist)
# # # 정답 리스트
# # correct_list1 = ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']
# # correct_list2 = ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']

# # correct_str1 = ['wbwbwbwb']
# # correct_str2 = ['bwbwbwbw']

# # 자르기 먼저

# list_list = []
# for i in range(n-7):
#     mini_list = []
#     for j in range(8):
#         mini_list.append(chesslist[i][i : 7 + i])

#     list_list.append(mini_list)


# print(list_list)


# # 함수를 만들어버리자
# def finddif1(list):
#     correct_list1 = ['wbwbwbwb']
#     dif = 0
#     for ele in list:
#         for i in correct_list1:
#             if ele == i:
#                 continue
#             else:
#                 dif += 1
#     return dif

# def finddif2(list):
#     correct_list2 = ['bwbwbwbw']
#     dif = 0
#     for ele in list:
#         for i in correct_list2:
#             if ele == i:
#                 continue
#             else:
#                 dif += 1
#     return dif


# # 비교해보기
# errs = []

# for i in range(len(list_list)):
#     err1 = 0
#     for j in range(0,4):
#         a = finddif1(list_list[i][2 * j])
#         b = finddif2(list_list[i][2 * j + 1])
#         err1 += a + b
#     err2 = 0
#     for j in range(0,4):
#         a = finddif2(list_list[i][2 * j])
#         b = finddif1(list_list[i][2 * j + 1])
#         err2 += a + b 
#     if err1 <= err2:
#         errs.append(err1)
#     else:
#         errs.append(err2)

# print(min(errs))
    


    

    



# import numpy as np

# n, m = map(int, input().split())

# chesslist = []

# for i in range(m):
#     np.row_list = list(input())
#     chesslist.append(np.row_list)

# np.correct_list1 = ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']
# np.correct_list2 = ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']

# print(np.equal(chesslist[0], np.correct_list1))
