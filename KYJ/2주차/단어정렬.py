# 1181번 단어 정렬

# ## 참고) sort 메서드는 사전순으로도 정렬해준다.
# a = ['it','im']
# a.sort()
# print(a)

N = int(input())    # 단어 개수
words = []
for i in range(N):
    words.append(input())   # input 받아서 리스트에 넣어주기

words = set(words) # 중복 없애기 위해 set로 변환
words = list(words)

words.sort() # 우선 사전 순으로 정렬
words.sort(key= lambda x: len(x))   # 사전순으로 정렬되어 있는 애들을 길이 기준으로 정렬해줌
for word in words:
    print(word)




# 딕셔너리를 이용해서 해볼려고 했는데
# 길이순으로는 출력이 어찌저찌 되는데 
# 사전순이 잘 안되서 포기
# N = int(input())
# words = []
# for i in range(N):
#     words.append(input())

# words = set(words)
# words = list(words)
 
# words_dict = {}
# for word in words:
#     words_dict[word] = len(word)

# new_dict = sorted(words_dict.items(), key = lambda x:x[1])

