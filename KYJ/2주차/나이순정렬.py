# 10814번 나이순 정렬

T = int(input())
people = [input().split() for _ in range(T)]

for person in people:
    person[0] = int(person[0])      # 정렬을 위해 나이를 정수로 바꿔줌

people.sort(key= lambda x: x[0])       #  sort에서 key를 이용해서 정렬 가능

for person in people:
    print(person[0],person[1])