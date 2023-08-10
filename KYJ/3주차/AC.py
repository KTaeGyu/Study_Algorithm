# 5430번 AC
'''
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. 
AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
D는 첫 번째 수를 버리는 함수이다.
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다.
예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 
최종 결과를 구하는 프로그램을 작성하시오.

'''

T = int(input())

for tc in range(1, T + 1):
    fun = input()       # 함수받아오기  
    n = int(input())    # 숫자개수

    input_list = input()                    # 우선 문자열로 받아온 후,
    input_list = input_list.strip('[')      # 문자열에서 [와 ]를 없애고
    input_list = input_list.strip(']')
    arr = input_list.split(',')             # ,를 기준으로 나눠서 리스트에 넣어줬다
    if arr[0].isdecimal():                  # 이때 [] 이런걸 처리하기 위해서 맨 앞에있는게 숫자인지를 확인
        arr = list(map(int, arr))
    else:
        arr = []


    # R이 나올 때마다 reverse를 해주면 시간 초과가 나므로,
    # R이 나오면 맨앞에 있는 인덱스를 뒤로 보냄
    top = 0     # 맨앞에 있는 인덱스
    cnt = 0     # R이 나오는 횟수(짝수번이면 그대로, 홀수번이면 뒤집기)
    is_true = True  # 길이가 0이 될때를 판단하기 위해
    
    try:    # 에러가 나면 바로 error출력하기
        for alpha in fun:
            if alpha == 'D':
                if len(arr) == 0:       # 지울려고 보니까 arr가 없다면, 에러
                    is_true = False
                    break
                arr.pop(top)    # 아니라면, 맨 앞에 있는걸 삭제
            elif alpha == 'R':  
                cnt += 1        
                if top:         # top이 맨 앞일 때는 맨 뒤로, 맨 뒤라면 맨 앞으로
                    top = 0
                else:
                    top = -1

        if cnt % 2 != 0:        # R이 나온 횟수가 짝,홀인지에 따라 문자열 뒤집기
            arr = arr[::-1]

        if is_true:             
            if len(arr) == 0:   # 다 지우고 없어진거면 []
                print('[]')
            else:               
                arr = list(map(str,arr))        # join을 쓰기위해 str로 바꿔줌
                print(f'[{",".join(arr)}]')
        else:
            print('error')
    
    except:
        print('error')


'''
덱 / 파싱 

그냥 손가는대로 했을 때, reverse를 쓰니 시간 초과가 나서
뒤집을 때 마다 top의 위치를 바꿔주는게 핵심인 것 같음
'''
