import sys
#sys.stdin = open("input.txt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
a = int(input())
for i in range(a):
    row, direct, extent = map(int, input().split())
    if direct == 0:
        for j in range(extent):
            #queue에 넣는방법 아닐것 같다.
            arr[row-1].append(arr[row-1].pop(0))
    else:
        for j in range(extent):
            arr[row-1].insert(0,arr[row-1].pop())


tmp = int(n/2)
cnt = -1
for i in range(n-1):
    #cnt += 1/ i가 cnt
    if i >= tmp+1:
        for j in range(0,n-i-1):
            arr[i][j] = 0
        #-1 넣는것에 테크닉도 신경써라
        for j in range(n-1,i,-1):
            arr[i][j] = 0
    else:
        for j in range(0,i):
            arr[i][j]=0
        for j in range(i):
            arr[i][n-j-1] = 0

answer=0
for i in arr:
    answer+=sum(i)
print(answer)