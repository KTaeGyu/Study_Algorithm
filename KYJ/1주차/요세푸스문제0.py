# 11866번 요세푸스 문제0

n, k = map(int,input().split())

# 사람들 번호로 리스트 생성
table = list(range(1,n+1))
# 결과 저장할 빈 리스트 생성
out_list = []

num = 0
# print('<',end = '')
for i in range(1,n+1):
    num = num + (k - 1) # 몇번째
    while num >= len(table):
        num -= len(table)
        
    element = table.pop(num)
    out_list.append(element)

print('<'+', '.join(map(str,out_list))+'>')


#     if i <= n-1:
#         print(element, end = ', ')
#     else:
#         print(element, end = '')

# print('>')

## 문제 푸는것도 푸는건데 출력이 머리가 아팠다..

## 몇 번째꺼를 없앨건지를 저렇게 말고 나머지를 이용해도 가능함


    


