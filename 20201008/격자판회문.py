import sys
# sys.stdin = open("input.txt")
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
arr = [list(map(int,input().split())) for _ in range(7)]
# tmp2 = arr[1:2][0] #리스트의 폐혜! 슬라이스의 폐혜! 가로로만 슬라이싱 되고 세로로는 슬라이싱이 안된다.
# print(tmp2) #ㅡㅡ
# print(arr[0][1:2]) #ㅡㅡ

cnt = 0
for i in range(7):
    for j in range(3):
        tmp = arr[i][j:j+5]
        if tmp == tmp[::-1]:
            cnt += 1
        # tmp2 = j+4
        if all(arr[j+k][i] == arr[j+4-k][i] for k in range(2)):
           cnt += 1
        # tmp2 = arr[j:j+5][i]
        # if tmp2 == tmp2[::-1]:
        #     cnt += 1
print(cnt)


