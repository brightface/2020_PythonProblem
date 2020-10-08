import sys
#sys.stdin = open("input.txt")

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
tmp = int(n/2)

for i in range(int(n/2)):
    for j in range(0,tmp):
        arr[i][j] = 0
        # for x in arr:
        #     print(x)
    for j in range(tmp, 0, -1):
        arr[i][n-j] = 0
    tmp -= 1
    if tmp < 0: tmp = int(n / 2)

#파이썬은 for문안에 조건문도 없고 변수 선언도 없다. 따라서. 변수선언은 반복문선언하기전에 따로 선언해줘야하고
#조건문을 하기 위해서 +=1을 따로 해줘야한다??. 이미 조건문이 만들어져 있으니까
cnt=0
for i in range(int(n/2)+1,n):
    cnt+=1
    for j in range(cnt):
        arr[i][j] = 0
        # for x in arr:
        #     print(x)
    for j in range(cnt, 0, -1):
        arr[i][n - j] = 0
ans=0
for i in arr:
    ans+=sum(i)
print(ans)