import sys
#아예 안되면 rt 감소 맞네
#되면 lt 증가시키고
#sys.stdin = open("input.txt")

n,c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
#print(arr)
arr.sort()
rt = arr[n-1]
lt=1
def Count(mid):
    #되나 검사.
    answer = False
    #마굿간 다 검사할 필요없다. 맨 앞에서만 검사하면 최대값 나온다.
    # for i in range(n-1):
    #     cnt = 1
    #     for j in range(i,n):
    #         if mid <=  arr[j]-arr[i]:
    #             cnt +=1
    #     if cnt >= c :
    #         answer = True
    # return answer
    cnt = 1
    for i in range(1,n): #여기가 잘못되었늗네;;
        if arr[i]-arr[0] >= mid: #여기가 잘못되었엇네 mid 보다 클떄 는 넣을수 있으니 참이다.
            cnt += 1
    if cnt >= c:
        answer = True
    return answer

res =0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid):
        res = mid
        lt=mid +1

    else :
        rt=mid -1

print(res)
