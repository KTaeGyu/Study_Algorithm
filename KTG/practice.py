import sys
sys.stdin = open("test.txt", "r")

R, C = map(int, input().split())
word = []
arr = [input() for _ in range(R)]
visited1 = [[0]*C for _ in range(R)]
visited2 = [[0]*C for _ in range(R)]
cnt = 0
def checkrow(x,y):
    global visited1
    oneword = ''
    for i in range(C):
        if x+i <= C-1:
            if arr[y][x+i] == '#':
                if len(oneword) != 1:
                    word.append(oneword)
                    break
            else:
                oneword += arr[y][x+i]
                visited1[y][x+i] = 1
                if x+i == C-1:
                    if len(oneword) != 1:
                        word.append(oneword)
                # print(visited,'a')
def checkcol(x,y):
    global visited2
    oneword2 = ''
    for i in range(R):
        if y+i <= R-1:
            if arr[y+i][x] == '#':
                if len(oneword2) != 1:
                    word.append(oneword2)
                    break
                break
            else:
                oneword2 += arr[y+i][x]
                visited2[y+i][x] = 1
                if y+i == R-1:
                    if len(oneword2) != 1:
                        word.append(oneword2)


for i in range(R):
    for j in range(C):
        if arr[i][j] == '#':
            visited1[i][j] = 1
            visited2[i][j] = 1

for i in range(R):
    for j in range(C):
        if arr[i][j] == '#':
            continue
        else:
            if not visited1[i][j]:
                checkrow(j,i)

for j in range(C):
    for i in range(R):
        if arr[i][j] == '#':
            continue
        else:
            if not visited2[i][j]:
                checkcol(j,i)

print(word)
word.sort()
print(word[0])