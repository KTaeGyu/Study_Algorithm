import sys
sys.stdin = open('../test.txt', 'r')

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
ans_lst = []
lst_arr = []
for row in arr:
    lst_arr.append(list(row))
    split_row = row.split('#')
    for split_one in split_row:
        if len(split_one) > 1:
            ans_lst.append(split_one)
turn_arr = list(zip(*lst_arr))
for col in turn_arr:
    str_col = ''
    for sen in col:
        str_col += sen
    split_col = str_col.split('#')
    for split_one in split_col:
        if len(split_one) > 1:
            ans_lst.append(split_one)
ans_lst.sort()
print(ans_lst[0])

