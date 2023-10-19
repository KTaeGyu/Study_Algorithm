# 백준 4673 '셀프 넘버'
# 구현문제

# 지울 수 구하는 함수
def self_n(i):
    global del_n
    if 1 <= i < 10:
        del_n = 2*i
    if 10 <= i < 100:
        del_n = i + (i//10) + (i % 10)
    if 100 <= i < 1000:
        del_n = i + (i//100) + ((i//10)%10) + (i%10)
    if 1000 <= i < 10000:
        del_n = i + (i//1000) + ((i//100)%10) + ((i//10)%10) + (i%10)

# 전체 리스트 만들기
arr =[]
for i in range(1, 10000):
    arr.append(i)
del_n = 0

#전체 리스트에서 하나씩 지우기
for i in range(1, 10001):
    self_n(i)
    if del_n in arr:
        arr.remove(del_n)

# 한줄씩 출력
for i in range(len(arr)):
    print(arr[i])


    # 지피티 풀이
    # def d(n):
    #     result = n
    #     for digit in str(n):
    #         result += int(digit)
    #     return result
    #
    #
    # numbers = list(range(1, 10001))
    # for i in range(1, 10001):
    #     if d(i) in numbers:
    #         numbers.remove(d(i))
    #
    # for num in numbers:
    #     print(num)
