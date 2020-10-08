import sys
sys.stdin = open("input.txt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]
A=int(input())

Arr= [list(map(int,input().split())) for _ in range(A)]
for i in Arr:
    i.insert(0,0)
    i.append(0)
# Arr.insert(0,[0 for i in range(A+2)])
# Arr.append([0 for i in range(A+2)])
Arr.insert(0,[0]*(A+2))
Arr.append([0]*(A+2))
for i in Arr:
    print(i)

answer= 0

for i in range(1,A+1):
    for j in range(1,A+1):
        # cnt=0
        # for x in range(4):
        #     if(Arr[i+dy[x]][j+dx[x]] < Arr[i][j]):
        #         cnt+=1
        # if cnt>=4:
        #     answer+=1
        if all(Arr[i][j] > Arr[i+dy[x]][j+dx[x]] for x in range(4)):
            answer += 1

print(answer)