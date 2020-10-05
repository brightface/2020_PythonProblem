import sys
#sys.stdin = open("input.txt")
n = int(input())
a = input().split()

flag = False
answer =0
cnt=1
for i in a:
    if i == '1':
        if flag == False:
            flag= True
            cnt = 1
            answer += cnt

        else:
            cnt += 1
            answer += cnt

    else :
        flag = False
print(answer)