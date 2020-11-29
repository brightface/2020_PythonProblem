import sys
sys.stdin=open("input.txt")

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0) #1차원 배열에 넣기
dy = [0]* (n+1)
dy[1]=1

res=0
for i in range(2,n+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[j]< arr[i] and dy[j]>max:
            max = dy[j] #메모리제이션 #학습은 어떻게 하는가? 이렇게 한다.
        #max찾은다음에 거기에 +1 해준다.
    dy[i]= max +1
    if dy[i]>res:
        res= dy[i]

print(res)


