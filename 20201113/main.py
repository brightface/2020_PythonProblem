import sys
sys.stdin = open("input.txt")
n=int(input())
#arr = [list(map(int, input().split()))] 안된다.
#arr = [map(int,input().split()] 도 안된다.
#맵이 묶어주는것이고 리스트함수로 해야 돼. 그냥 바로 위처럼 []연산자로 리스트 생성시는 안됨.
arr = list(map(int, input().split()))
#print(arr, n)
p = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if p[j] == 0 and arr[i-1] == 0:
            p[j] = i
            break
        elif p[j] == 0:
            arr[i-1] -= 1
p.pop(0)
for k in p:
    print(k, end=' ')