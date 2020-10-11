import sys
# sys.stdin = open("input.txt")
n,m = map(int, input().split())
arr= list(map(int,input().split()))
arr.sort()
# print(arr)

lt = 0
rt = n-1
answer = -1
while(lt<=rt):
    mid = (lt+rt)//2
    if arr[mid] == m:
        answer = mid
        break
    elif arr[mid] < m:
        lt = mid + 1
    else :
        rt = mid - 1
print(answer+1)