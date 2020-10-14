import sys
#sys.stdin = open("input.txt")

n,m = map(int, input().split())
arr= list(map(int,input().split()))

arr.sort()
check = [0]*(n)
lt =0
rt = n-1
cnt=0
while arr: #empty() 함수
    # if lt == rt:
    #     cnt+=1
    #     break
    # if check[lt] !=0:
    #     lt+=1
    # if check[rt] != 0:
    #     rt-=1
    if len(arr) == 1:
        cnt+=1
        break
    if arr[0]+arr[-1] <= m:
        arr.pop()
        arr.pop(0)
        cnt+=1
    else:
        arr.pop()
        cnt+=1
        #     cnt+=1
        # else:
        #     lt+=1
        #     rt-=1
        #     if arr[lt] + arr[rt] <= m:
        #         arr.pop()
        #         cnt+=1

    #조건을 생각해라.
    #그리고 문제에서 요구하는 답을 생각해라.
    #문제에서 요구하는 조건에 따른 답을 해결하는데 있어서
    #조건에 맞는답은?
    #거기에 힌트와 논리가 있따.
    #여기서는 제일 무거운사람과 가벼운사람이 동시에 못타면 무거운사람 혼자타야돼 반드시 . 다 구출해야하니까. 그게 문제의 목적

print(cnt)
