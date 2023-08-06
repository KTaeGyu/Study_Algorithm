# 1259번, 팰린드롬수
 

while True: # 반복하기 위해 while
    num = list(map(int,input())) # 뒤집어야하니까 편하게 리스트로 받아줌
    if num == [0]:  # 0을 input으로 받으면 끝나야하므로
        break
    re_num = num[::-1] # 리스트 뒤집은거
    if re_num == num:
        print('yes')
    else:
        print('no')